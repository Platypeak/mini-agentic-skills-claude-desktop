---
name: project-creation
description: >
  Use this skill whenever the user wants to create a brand-new project from scratch using a
  natural language description. Triggers include: "build me a X project", "create a new Y app",
  "scaffold a Z system", "start a project for...", "generate a boilerplate for...", or any
  request to create a fresh codebase from nothing. Claude will parse the intent, present an
  architecture plan for confirmation, then generate all files, zip them, and present the
  download. New stack templates can be added to the templates/ folder and referenced here.
  Scope: Flask/Firebase backends, PyQt6 desktop apps, Android Jetpack Compose apps,
  PHP/MySQL web apps, and any ad-hoc stack described in natural language.
---

# Project Creation Skill

Claude generates **complete, ready-to-run project scaffolds** from a natural language description —
architecture plan first, full file generation second, ZIP delivery third.

---

## Trigger Detection

This skill activates when the user says things like:
- "build me a Flask project for..."
- "create a new Android app that..."
- "scaffold a PyQt6 desktop app with..."
- "start a PHP project for..."
- "generate a boilerplate for a [stack] system"
- "make me a new project for [purpose]"

**Do NOT trigger** for: editing existing files (→ use project-settlement), writing a single script,
or answering a code question without file generation intent.

---

## Workflow

### Step 1 — Parse the Intent

From the user's prompt, extract:

| Field | What to identify |
|---|---|
| **Stack** | Language, framework, DB, platform |
| **Purpose** | What the app does (HR system, bulk mailer, logistics panel, etc.) |
| **Key Features** | Main modules, screens, API endpoints, or UI flows mentioned |
| **Conventions** | Any style preferences (camelCase, REST vs Firebase, auth method, etc.) |

If the stack is **ambiguous or unspecified**, ask one clarifying question before proceeding:
> "What stack do you want? (e.g. Flask+Firebase, PyQt6, Android Compose, PHP+MySQL)"

---

### Step 2 — Match to a Template

Check if a template exists for the detected stack:

| Stack Keywords | Template Folder |
|---|---|
| flask, firebase, python backend, REST API | `templates/flask-firebase/` |
| pyqt, pyqt6, desktop, qt app | `templates/pyqt6-app/` |
| android, jetpack, compose, kotlin | `templates/android-compose/` |
| php, mysql, web panel, admin panel | `templates/php-mysql/` |
| anything else | Generate ad-hoc (no template base) |

Templates live at: `/mnt/skills/user/project-creation/templates/<stack>/`

Read the template's `_TEMPLATE_META.md` to understand what it provides and what to customize.

---

### Step 3 — Present Architecture Plan (ALWAYS do this before generating files)

Before writing a single file, output a structured plan in this format:

```
## 📐 Architecture Plan

**Project:** <n>
**Stack:** <stack>
**Purpose:** <one-line description>

### Folder Structure
<show the full intended directory tree>

### Files to Generate
<list each file with a one-line description of what it does>

### What You'll Still Need to Do
<list any manual steps: env vars, API keys, installs, device setup, etc.>

---
Shall I generate this? (say yes / or ask me to adjust anything)
```

**Wait for user confirmation before proceeding to Step 4.**

---

### Step 4 — Generate All Files

Work directory: `/home/claude/project/<project-name>/`

```bash
mkdir -p /home/claude/project/<project-name>
```

#### 4a — If a template exists:

Copy the template base into the work directory first:

```bash
cp -r /mnt/skills/user/project-creation/templates/<stack>/ /home/claude/project/<project-name>/
```

Then customize every templated file:
- Replace `{{PROJECT_NAME}}` with actual project name
- Replace `{{DESCRIPTION}}` with user's purpose
- Replace `{{AUTHOR}}` with user's name if known, else leave blank
- Add any feature-specific files beyond the template base

#### 4b — If no template (ad-hoc stack):

Generate all files from scratch using `create_file`. Follow these conventions:
- Always include `README.md` with setup instructions
- Always include `.gitignore` appropriate to the stack
- Always include a root config file (`requirements.txt`, `package.json`, `build.gradle`, `composer.json`, etc.)
- Group files logically into subfolders (don't dump everything in root)

---

### Step 5 — Verify & Lint

After generating all files, do a quick self-check:

```bash
# Count generated files
find /home/claude/project/<project-name>/ -type f | wc -l

# Show final tree
find /home/claude/project/<project-name>/ -type f | sort
```

Check:
- [ ] All imports in code files reference real files that exist in the project
- [ ] No placeholder text like `TODO`, `YOUR_KEY_HERE` left without a comment explaining it
- [ ] `README.md` exists and has accurate setup steps
- [ ] Root dependency file exists (`requirements.txt`, `package.json`, etc.)

---

### Step 6 — Zip and Deliver

```bash
cd /home/claude/project/
zip -r /mnt/user-data/outputs/<project-name>.zip <project-name>/
```

Then call `present_files` with the ZIP path.

Follow up with a short post-generation summary:

```
✅ <N> files generated

📦 Download: <project-name>.zip

🔧 To get started:
  1. <first manual step>
  2. <second manual step>
  ...
```

---

## Rules

1. **Always show the architecture plan first** — never generate files without user confirmation
2. **Use templates when available** — don't reinvent; customize from the base
3. **Always include README.md and .gitignore** — every project gets these, no exceptions
4. **Never leave broken imports** — if you reference a module, the file must exist in the output
5. **ZIP the whole project folder** — user gets one file to download, not scattered files
6. **Present only the ZIP** via `present_files` — not individual files unless the user asks
7. **Add inline comments in code** — especially in config files and anything with secrets/env vars
8. **Keep templates generic** — don't hardcode project-specific names inside template files; use `{{PLACEHOLDERS}}`

---

## Adding New Templates

To add a new stack template:

1. Create a folder: `templates/<stack-name>/`
2. Add a `_TEMPLATE_META.md` inside it (see format below)
3. Add all base files with `{{PLACEHOLDERS}}` for project-specific values
4. Add the stack to the **Match to a Template** table in Step 2 of this SKILL.md

### `_TEMPLATE_META.md` Format

```markdown
# Template: <Stack Name>

## What This Provides
<List of files and what each does>

## Placeholders
| Placeholder | Replaced With |
|---|---|
| {{PROJECT_NAME}} | The project folder/package name |
| {{DESCRIPTION}} | One-line app description |
| {{AUTHOR}} | Developer name |

## Manual Steps After Generation
<Steps the user must do that can't be automated>
```

---

## Edge Cases

- **User gives very vague prompt** ("make me an app"): Ask for stack + purpose before planning
- **User asks for a feature not in the template**: Generate extra files beyond the template base; document them in the summary
- **Conflicting stack signals** ("Flask with React frontend"): Note both in the plan and scaffold both sides
- **User rejects the plan**: Adjust the plan based on feedback and re-present; do not start generating
- **Very large project requested** (20+ files): Break generation into logical groups and confirm after each group
