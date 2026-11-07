"use strict";
const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const os = require("node:os");
const path = require("node:path");
const { inspect } = require("../skills/shared-investigations/scripts/investigations.cjs");

function fixture(t) {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), "shared-investigation-"));
  t.after(() => fs.rmSync(root, { recursive: true, force: true }));
  const write = (relative, value) => {
    const target = path.join(root, relative);
    fs.mkdirSync(path.dirname(target), { recursive: true });
    fs.writeFileSync(target, typeof value === "string" ? value : JSON.stringify(value, null, 2) + "\n");
  };
  const registry = { schemaVersion: 1, sources: [{ id: "draft-study", title: "Fictional draft study", owner: "Research team",
    location: "https://example.org/draft-study", revision: "study-3", access: "shared" }], investigations: [{
    id: "draft-recovery", title: "Recovering unsaved drafts", question: "Where does recovery fail?", status: "open", coordinator: "Casey",
    contributors: ["Morgan", "Riley"], record: "investigations/draft-recovery/README.md", sourceIds: ["draft-study"], contributions: [] }] };
  write(registry.investigations[0].record, "# Draft recovery\nCurrent findings remain uncertain.\n");
  const save = () => write("investigations/registry.json", registry);
  function contribute(id, author, sourceIds = ["draft-study"], newArtifactSourceIds = []) {
    const parent = `investigations/draft-recovery/contributions/${id}`;
    const manifest = parent + "/contribution.json";
    const data = { schemaVersion: 1, id, investigationId: "draft-recovery", contributor: author, kind: "finding",
      summary: "README.md", sourceIds, sourceRevisions: Object.fromEntries(sourceIds.map((id) => [id, registry.sources.find((s) => s.id === id).revision])), newArtifactSourceIds };
    write(parent + "/README.md", "# Fictional contribution\nMethod, finding, uncertainty and source references.\n");
    write(manifest, data); registry.investigations[0].contributions.push(manifest); save();
    return { parent, manifest, data };
  }
  save(); return { root, write, registry, save, contribute };
}

test("two contributors can cite one existing source and add a separately maintained new artifact", (t) => {
  const f = fixture(t);
  f.contribute("study-review", "Morgan");
  const local = "investigations/draft-recovery/contributions/reproduction/artifacts/result.json";
  f.write(local, { fictional: true, failures: 2, attempts: 8 });
  f.registry.sources.push({ id: "reproduction-result", title: "Independent fictional reproduction", owner: "Riley", location: local, revision: "run-1", access: "shared" });
  f.registry.investigations[0].sourceIds.push("reproduction-result");
  f.contribute("reproduction", "Riley", ["draft-study", "reproduction-result"], ["reproduction-result"]);
  const result = inspect(f.root);
  assert.deepEqual(result.errors, []);
  assert.equal(result.investigations[0].contributions, 2);
  assert.equal(f.registry.sources.filter((s) => s.location.startsWith("https:")).length, 1);
  assert.equal(fs.existsSync(path.join(f.root, "evidence")), false);
});

test("checking and listing never change workspace files or fetch an external source", (t) => {
  const f = fixture(t);
  f.registry.sources[0].location = "https://unreachable.invalid/study"; f.save();
  const registry = fs.readFileSync(path.join(f.root, "investigations/registry.json"));
  const record = fs.readFileSync(path.join(f.root, f.registry.investigations[0].record));
  assert.deepEqual(inspect(f.root).errors, []);
  assert.deepEqual(fs.readFileSync(path.join(f.root, "investigations/registry.json")), registry);
  assert.deepEqual(fs.readFileSync(path.join(f.root, f.registry.investigations[0].record)), record);
});

test("duplicate source identities and competing declarations of one location fail", (t) => {
  const f = fixture(t);
  f.registry.sources.push({ ...f.registry.sources[0] }); f.save();
  assert.ok(inspect(f.root).errors.some((s) => s.includes("Duplicate source ID")));
  f.registry.sources[1].id = "other-source"; f.save();
  assert.ok(inspect(f.root).errors.some((s) => s.includes("same maintained location")));
});

test("missing attribution, a foreign investigation and undeclared evidence fail", (t) => {
  const f = fixture(t), c = f.contribute("study-review", "Morgan");
  for (const patch of [{ contributor: "" }, { contributor: "Unknown" }, { investigationId: "other" }, { sourceIds: ["missing"] }]) {
    f.write(c.manifest, { ...c.data, ...patch });
    assert.ok(inspect(f.root).errors.length);
  }
});

test("an existing external report cannot be declared a new local contribution artifact", (t) => {
  const f = fixture(t);
  f.contribute("study-review", "Morgan", ["draft-study"], ["draft-study"]);
  assert.ok(inspect(f.root).errors.some((s) => s.includes("inside its contribution directory")));
});

test("private paths, traversal, missing local evidence and embedded URL credentials fail", (t) => {
  const f = fixture(t);
  for (const location of ["../outside.txt", ".local/sources.json", "missing.json", "https://user:secret@example.org/study"]) {
    f.registry.sources[0].location = location; f.save();
    assert.ok(inspect(f.root).errors.length);
  }
});

test("summary paths cannot escape a contribution directory", (t) => {
  const f = fixture(t), c = f.contribute("study-review", "Morgan");
  f.write(c.manifest, { ...c.data, summary: "../README.md" });
  assert.ok(inspect(f.root).errors.some((s) => s.includes("inside its contribution directory")));
});

test("a restricted source requires an explicit access limitation", (t) => {
  const f = fixture(t); f.registry.sources[0].access = "restricted"; f.save();
  assert.ok(inspect(f.root).errors.some((s) => s.includes("accessNote")));
  f.registry.sources[0].accessNote = "Requires an authorized research account."; f.save();
  assert.deepEqual(inspect(f.root).errors, []);
});

test("missing IDs cannot accidentally become the string undefined", (t) => {
  const f = fixture(t); delete f.registry.sources[0].id; f.save();
  assert.ok(inspect(f.root).errors.length);
});

test("declared symlinks cannot direct the checker outside the workspace", { skip: process.platform === "win32" }, (t) => {
  const f = fixture(t);
  fs.symlinkSync(os.tmpdir(), path.join(f.root, "linked"));
  f.registry.sources[0].location = "linked/outside.json"; f.save();
  assert.ok(inspect(f.root).errors.length);
});


test("a contribution retains its inspected revision when current evidence advances", (t) => {
  const f = fixture(t), c = f.contribute("study-review", "Morgan");
  f.registry.sources[0].revision = "study-4"; f.save();
  assert.deepEqual(inspect(f.root).errors, []);
  assert.equal(JSON.parse(fs.readFileSync(path.join(f.root, c.manifest))).sourceRevisions["draft-study"], "study-3");
  f.write(c.manifest, { ...c.data, sourceRevisions: {} });
  assert.ok(inspect(f.root).errors.some((s) => s.includes("inspected revision")));
});
