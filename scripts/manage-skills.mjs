#!/usr/bin/env node

import { spawnSync } from 'node:child_process';
import fs from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const codexRoot = process.env.CODEX_HOME || path.join(os.homedir(), '.codex');

function parseArgs(argv) {
  const args = [...argv];
  const command = args.shift() || 'status';
  let dest = path.join(codexRoot, 'skills');

  while (args.length) {
    const flag = args.shift();
    if (flag === '--dest' && args.length) dest = path.resolve(args.shift());
    else throw new Error(`Unknown or incomplete option: ${flag}`);
  }

  return { command, dest };
}

async function exists(filePath) {
  try {
    await fs.lstat(filePath);
    return true;
  } catch (error) {
    if (error.code === 'ENOENT') return false;
    throw error;
  }
}

async function discoverSkills() {
  const entries = await fs.readdir(repoRoot, { withFileTypes: true });
  const skills = [];

  for (const entry of entries) {
    if (!entry.isDirectory() || entry.name.startsWith('.')) continue;
    const source = path.join(repoRoot, entry.name);
    if (await exists(path.join(source, 'SKILL.md'))) skills.push({ name: entry.name, source });
  }

  return skills.sort((a, b) => a.name.localeCompare(b.name));
}

async function inspectTarget(skill, dest) {
  const target = path.join(dest, skill.name);

  try {
    const stat = await fs.lstat(target);
    if (!stat.isSymbolicLink()) return { state: 'conflict', target, detail: 'target exists and is not a symlink' };

    const link = await fs.readlink(target);
    const resolved = path.resolve(path.dirname(target), link);
    if (resolved === skill.source) return { state: 'linked', target };
    return { state: 'conflict', target, detail: `symlink points to ${resolved}` };
  } catch (error) {
    if (error.code === 'ENOENT') return { state: 'missing', target };
    throw error;
  }
}

function printResult(skill, result) {
  const labels = { linked: 'OK', missing: 'MISSING', created: 'CREATED', conflict: 'CONFLICT' };
  const detail = result.detail ? ` — ${result.detail}` : '';
  console.log(`${labels[result.state].padEnd(8)} ${skill.name}${detail}`);
}

async function status(dest) {
  const skills = await discoverSkills();
  if (!skills.length) throw new Error(`No top-level skill directories found in ${repoRoot}`);

  let conflicts = 0;
  let missing = 0;
  for (const skill of skills) {
    const result = await inspectTarget(skill, dest);
    printResult(skill, result);
    if (result.state === 'conflict') conflicts += 1;
    if (result.state === 'missing') missing += 1;
  }

  console.log(`\n${skills.length} skill(s): ${conflicts} conflict(s), ${missing} missing.`);
  return conflicts ? 1 : 0;
}

async function sync(dest) {
  const skills = await discoverSkills();
  if (!skills.length) throw new Error(`No top-level skill directories found in ${repoRoot}`);
  await fs.mkdir(dest, { recursive: true });

  let conflicts = 0;
  for (const skill of skills) {
    const result = await inspectTarget(skill, dest);
    if (result.state === 'missing') {
      await fs.symlink(skill.source, result.target, 'dir');
      printResult(skill, { ...result, state: 'created' });
    } else {
      printResult(skill, result);
      if (result.state === 'conflict') conflicts += 1;
    }
  }

  if (conflicts) console.error(`\nStopped with ${conflicts} conflict(s). Existing targets were not changed.`);
  return conflicts ? 1 : 0;
}

async function validate() {
  const skills = await discoverSkills();
  const validator = path.join(codexRoot, 'skills', '.system', 'skill-creator', 'scripts', 'quick_validate.py');
  if (!(await exists(validator))) throw new Error(`Codex skill validator not found: ${validator}`);

  let failures = 0;
  for (const skill of skills) {
    const result = spawnSync('python3', [validator, skill.source], { encoding: 'utf8' });
    if (result.status === 0) console.log(`OK       ${skill.name}`);
    else {
      failures += 1;
      console.error(`INVALID  ${skill.name}`);
      if (result.stdout.trim()) console.error(result.stdout.trim());
      if (result.stderr.trim()) console.error(result.stderr.trim());
    }
  }

  console.log(`\n${skills.length} skill(s): ${failures} validation failure(s).`);
  return failures ? 1 : 0;
}

async function update(dest) {
  const validationCode = await validate();
  if (validationCode) return validationCode;
  return sync(dest);
}

async function selfTest() {
  const tempDest = await fs.mkdtemp(path.join(os.tmpdir(), 'wdskills-'));
  try {
    if (await sync(tempDest)) throw new Error('initial sync failed');
    if (await status(tempDest)) throw new Error('status after sync failed');

    const [first] = await discoverSkills();
    const target = path.join(tempDest, first.name);
    await fs.unlink(target);
    await fs.mkdir(target);
    const conflict = await inspectTarget(first, tempDest);
    if (conflict.state !== 'conflict') throw new Error('real-directory conflict was not detected');

    console.log('\nSELF-TEST PASSED');
    return 0;
  } finally {
    await fs.rm(tempDest, { recursive: true, force: true });
  }
}

async function main() {
  const { command, dest } = parseArgs(process.argv.slice(2));
  if (command === 'update') return update(dest);
  if (command === 'status') return status(dest);
  if (command === 'sync') return sync(dest);
  if (command === 'validate') return validate();
  if (command === 'test') return selfTest();
  throw new Error('Usage: manage-skills.mjs <update|status|sync|validate|test> [--dest PATH]');
}

main()
  .then(code => { process.exitCode = code; })
  .catch(error => {
    console.error(`ERROR: ${error.message}`);
    process.exitCode = 1;
  });
