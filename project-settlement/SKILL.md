---
name: project-settlement
description: >
  Use this skill whenever the user uploads a project ZIP file and asks Claude to make changes,
  fix bugs, edit specific files, or modify any part of their codebase. Instead of reading the
  entire project, Claude identifies only the files relevant to the task, extracts just those
  files into the sandbox using a targeted extraction script, edits them, and presents the
  modified files back to the user. Trigger this skill when the user says things like "here's
  my project zip, can you fix...", "edit this file in my project", "update the code in my
  uploaded project", "change X in my codebase", or any variation of working with an uploaded
  project archive. Scope: Python/Flask backends, PHP web projects, HTML/JS/CSS frontends.
---

# Project Settlement Skill

Claude works **surgically** on projects — read only what's needed, edit only what's needed, present only what changed.

---

## Workflow

### Step 1 — Locate the ZIP

The user will have uploaded a `.zip` file. It will be at:
```
/mnt/user-data/uploads/<filename>.zip
```

Run a quick listing to confirm:
```bash
ls /mnt/user-data/uploads/
```

---

### Step 2 — Peek at the project structure (without full extraction)

Before extracting anything, run a **non-extracting** tree view of the ZIP to understand the layout:

```bash
python3 -c "
import zipfile, sys
with zipfile.ZipFile('/mnt/user-data/uploads/<filename>.zip') as z:
    for name in sorted(z.namelist()):
        print(name)
"
```

Use this listing — combined with the user's task description — to decide which files are needed. **Do not extract the entire project.** Be minimal.

---

### Step 3 — Identify needed files

Based on the task, select the smallest set of files required. Guidelines by project type:

| Project Type | Typical files to touch |
|---|---|
| Python / Flask | `app.py`, relevant route file, `models.py`, `templates/*.html` |
| PHP | The specific `.php` file(s) mentioned or implied, plus any included files |
| HTML / JS / CSS | The specific `.html`, `.js`, or `.css` files relevant to the UI change |

**Rule:** If a file doesn't need to be read or modified to complete the task — skip it.

---

### Step 4 — Write and run the extraction script

Write a Python extraction script that extracts the **entire ZIP** into `/home/claude/project/`, preserving folder structure:

```python
import zipfile
import os

ZIP_PATH = "/mnt/user-data/uploads/<filename>.zip"
OUTPUT_DIR = "/home/claude/project"

os.makedirs(OUTPUT_DIR, exist_ok=True)

with zipfile.ZipFile(ZIP_PATH) as z:
    z.extractall(OUTPUT_DIR)
    print(f"Extracted {len(z.namelist())} files to {OUTPUT_DIR}")
```

Run the script and confirm extraction succeeds before proceeding.

---

### Step 5 — Read and edit

- Read only the extracted files using the `view` tool
- Make all edits using `str_replace` (preferred for surgical changes) or `create_file` (for full rewrites)
- Work entirely within `/home/claude/project/`
- **Do not re-extract or read files you don't need to change**

---

### Step 6 — Present the modified files

When all edits are done, copy only the **modified files** to `/mnt/user-data/outputs/` and call `present_files`:

```bash
cp /home/claude/project/app.py /mnt/user-data/outputs/app.py
# repeat for each modified file
```

Then call `present_files` with the list of output paths.

**Do NOT re-zip the project or present unmodified files.**

---

## Rules

1. **Always extract the whole ZIP** — use `z.extractall()`, never partial extraction
2. **Never read files you don't need** — the project may have dozens of files; only `view` the relevant ones identified in Step 3
3. **Never present unmodified files** — only show the user what actually changed
4. **Prefer `str_replace` over full rewrites** when only a few lines change
5. **One extraction script per task** — write it fresh each time, tailored to the ZIP filename
6. **If you can't find a file after extraction**, tell the user immediately rather than guessing

---

## Edge Cases

- **Nested ZIPs or subdirectory roots**: The ZIP may wrap everything in a root folder (e.g., `myproject/src/app.py`). Always check the full path from the ZIP listing in Step 2, and use exact paths in the extraction script.
- **Binary or media files**: Never extract images, fonts, or other binary assets unless explicitly asked.
- **Multiple files with the same name**: If the same filename exists at different paths (e.g., two `index.html` files), clarify with the user which one to edit before proceeding.
- **User doesn't know the exact filename**: If the user gives a vague description ("the main page"), use the ZIP listing to identify the best candidate and confirm with the user if unsure.
