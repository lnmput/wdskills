#!/usr/bin/env node

import fs from 'fs/promises';
import path from 'path';
import os from 'os';
import { fileURLToPath } from 'url';
import prompts from 'prompts';

// Setup file paths
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const workspaceRoot = path.resolve(__dirname, '..');

async function parseSkillMetadata(skillDir) {
  const skillPath = path.join(skillDir, 'SKILL.md');
  try {
    const content = await fs.readFile(skillPath, 'utf8');
    const match = content.match(/^---\r?\n([\s\S]*?)\r?\n---/);
    let name = path.basename(skillDir);
    let description = '';
    if (match) {
      const frontmatter = match[1];
      const lines = frontmatter.split('\n');
      for (const line of lines) {
        const parts = line.split(':');
        if (parts.length >= 2) {
          const key = parts[0].trim();
          const value = parts.slice(1).join(':').trim();
          if (key === 'name') name = value;
          if (key === 'description') description = value;
        }
      }
    }
    return { name, description, dirName: path.basename(skillDir), path: skillDir };
  } catch (err) {
    return { name: path.basename(skillDir), description: '', dirName: path.basename(skillDir), path: skillDir };
  }
}

async function run() {
  console.log('\x1b[36m%s\x1b[0m', '🔍 Scanning for custom skills in workspace...');

  // 1. Scan root directory for skill directories
  const files = await fs.readdir(workspaceRoot, { withFileTypes: true });
  const skillPromises = files
    .filter(file => file.isDirectory() && !file.name.startsWith('.') && file.name !== 'node_modules' && file.name !== 'bin')
    .map(async file => {
      const fullPath = path.join(workspaceRoot, file.name);
      try {
        await fs.access(path.join(fullPath, 'SKILL.md'));
        return await parseSkillMetadata(fullPath);
      } catch {
        return null;
      }
    });

  const skills = (await Promise.all(skillPromises)).filter(Boolean);

  if (skills.length === 0) {
    console.log('\x1b[31m%s\x1b[0m', '❌ No skills (directories containing SKILL.md) found in this project.');
    process.exit(0);
  }

  console.log('\x1b[32m%s\x1b[0m', `Found ${skills.length} skill(s) ready to install.\n`);

  // 2. Ask user for destination directory
  const destinationChoices = [];

  // Add workspace option first
  destinationChoices.push({
    title: 'Workspace (Available only in this project)',
    value: path.resolve(process.cwd(), '.agents/skills'),
    description: './.agents/skills/'
  });

  // Detect and add all existing global directories
  const globalPaths = [
    { title: 'Global (Codex)', path: path.resolve(os.homedir(), '.codex/skills') },
    { title: 'Global (Gemini)', path: path.resolve(os.homedir(), '.gemini/skills') },
    { title: 'Global (Gemini Config)', path: path.resolve(os.homedir(), '.gemini/config/skills') }
  ];

  for (const gp of globalPaths) {
    try {
      await fs.access(gp.path);
      destinationChoices.push({
        title: gp.title,
        value: gp.path,
        description: gp.path.replace(os.homedir(), '~')
      });
    } catch {}
  }

  // Add custom path option
  destinationChoices.push({
    title: 'Custom Directory...',
    value: 'custom',
    description: 'Enter a custom absolute directory path manually'
  });

  const targetResponse = await prompts({
    type: 'select',
    name: 'destDir',
    message: 'Where would you like to install the skills?',
    choices: destinationChoices,
    initial: 0
  });

  if (!targetResponse.destDir) {
    console.log('Installation cancelled.');
    process.exit(0);
  }

  // Determine target path
  let destDir = targetResponse.destDir;

  if (destDir === 'custom') {
    const customResponse = await prompts({
      type: 'text',
      name: 'customPath',
      message: 'Enter the absolute path to the directory:',
      validate: value => value ? true : 'Path cannot be empty'
    });
    
    if (!customResponse.customPath) {
      console.log('Installation cancelled.');
      process.exit(0);
    }
    
    destDir = path.resolve(customResponse.customPath.replace(/^~/, os.homedir()));
  }

  // 3. Ask user which skills to install
  const skillChoices = skills.map(skill => ({
    title: skill.name,
    value: skill,
    description: skill.description || 'No description provided',
    selected: true // default all selected
  }));

  const selectionResponse = await prompts({
    type: 'multiselect',
    name: 'selectedSkills',
    message: 'Select the skills you want to install:',
    choices: skillChoices,
    hint: '- Space to select/deselect. Return to confirm.'
  });

  const selectedSkills = selectionResponse.selectedSkills;
  if (!selectedSkills || selectedSkills.length === 0) {
    console.log('No skills selected. Installation cancelled.');
    process.exit(0);
  }

  // 4. Install selected skills
  console.log('\n\x1b[36m%s\x1b[0m', `📦 Installing to: ${destDir}...`);
  await fs.mkdir(destDir, { recursive: true });

  for (const skill of selectedSkills) {
    const targetSkillPath = path.join(destDir, skill.dirName);
    console.log(`Copying ${skill.name} -> ${targetSkillPath}...`);
    // Ensure destination skill path is clean
    await fs.rm(targetSkillPath, { recursive: true, force: true });
    // Copy the skill directory
    await fs.cp(skill.path, targetSkillPath, { recursive: true });
  }

  console.log('\n\x1b[32m%s\x1b[0m', '✅ Installation completed successfully!');
  console.log('You may need to reload or restart your agent environment to load the new skills.');
}

run().catch(err => {
  console.error('\x1b[31m%s\x1b[0m', 'An error occurred during installation:', err);
  process.exit(1);
});
