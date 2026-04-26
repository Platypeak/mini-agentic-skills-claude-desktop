# 🤖 Mini Agentic Skills — Claude Desktop

> **Plug-and-play skill files that make Claude Desktop smarter, faster, and more agentic.**

![Claude Desktop](https://img.shields.io/badge/Claude-Desktop-blueviolet?style=for-the-badge&logo=anthropic)
![Skills](https://img.shields.io/badge/Skills-3-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)
![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-orange?style=for-the-badge)

---

## ✨ What is this?

This repo is a collection of **skill files** for [Claude Desktop](https://claude.ai/download) — structured markdown instructions that teach Claude how to handle specific tasks with precision and consistency.

Drop a skill into your Claude Desktop config and Claude will automatically know **when** to use it and **how** to execute it — like giving Claude a mini operations manual for a specific job.

---

## 📦 Skills Available

| Skill | Description | Scope |
|---|---|---|
| 🗂️ [project-settlement](./project-settlement/SKILL.md) | Surgically edit uploaded project ZIPs without reading the whole codebase | PHP, Python/Flask, HTML/JS/CSS |
| 🏗️ [project-creation](./project-creation/SKILL.md) | Scaffold new projects from scratch with proper structure, config files, and boilerplate | PHP, Python, HTML/JS/CSS |
| 🎨 [web-design-ultra-pro-max](./web-design-ultra-pro-max/SKILL.md) | Generate world-class, agency-grade websites with cinematic animations, editorial layouts, and premium UX — never generic AI slop | Single-file HTML/CSS/JS or React JSX |

> More skills coming soon. Star ⭐ the repo to stay updated!

---

## 🚀 How to Use

### Step 1 — Clone or download the repo

```bash
git clone https://github.com/Platypeak/mini-agentic-skills-claude-desktop.git
```

### Step 2 — Point Claude Desktop to the skills folder

Open (or create) your `claude_desktop_config.json` file:

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

Add the skills directory so Claude can read them at runtime:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/path/to/mini-agentic-skills-claude-desktop"
      ]
    }
  }
}
```

> Replace `/path/to/mini-agentic-skills-claude-desktop` with the actual path where you cloned the repo.

### Step 3 — Just talk to Claude

Once a skill is loaded, Claude will automatically trigger it when your message matches the skill's use case. No commands, no setup — just natural conversation.

**Example triggers:**
- *"Build me a landing page for my SaaS"* → triggers `web-design-ultra-pro-max`
- *"Create a new PHP project called blog-app"* → triggers `project-creation`
- *"Fix the login bug in my uploaded project ZIP"* → triggers `project-settlement`

---

## 🧠 How Skills Work

Each skill is a `SKILL.md` file inside its own folder. It contains:

- **A YAML front matter block** — tells Claude *when* to trigger the skill (name + description)
- **A step-by-step workflow** — tells Claude *how* to execute the task
- **Rules & edge cases** — guardrails to keep Claude precise and on-brand

```
mini-agentic-skills-claude-desktop/
│
├── project-settlement/
│   └── SKILL.md          ← Handles uploaded ZIP project edits
│
├── project-creation/
│   ├── SKILL.md          ← Scaffolds new projects from scratch
│   └── templates/        ← Starter templates used by the skill
│
├── web-design-ultra-pro-max/
│   └── SKILL.md          ← Generates premium animated websites
│
└── README.md
```

---

## 🛠️ Skill Breakdown

### 🗂️ project-settlement
Surgically edits files inside uploaded project ZIPs. Claude reads only what it needs, applies targeted changes, and hands back a clean ZIP — without hallucinating the rest of the codebase.

**Triggers:** uploading a ZIP + asking for a fix, edit, or feature addition.

---

### 🏗️ project-creation
Scaffolds brand-new projects with the right folder structure, config files, `.gitignore`, `README`, and boilerplate code — tailored to the stack you ask for.

**Triggers:** "create a new project", "scaffold a [framework] app", "set up a fresh [language] project".

---

### 🎨 web-design-ultra-pro-max
Generates complete, single-file websites that look like they were built by a top-tier creative agency. Every output includes:
- Custom animated cursor
- Word-by-word or character-by-character headline entrances
- Scroll-triggered reveal animations (IntersectionObserver)
- Magnetic CTA buttons
- Marquee / ticker strips
- Parallax layers
- Responsive mobile breakpoints
- A deliberate color palette (never generic purple-on-white)
- Fonts with actual character (Playfair, Bebas Neue, Syne, etc.)

**Triggers:** "design me a website", "build a landing page", "make a portfolio", "create a product page".

---

## 🤝 Contributing

Got a skill idea? PRs are welcome!

1. Fork the repo
2. Create a folder with your skill name (kebab-case)
3. Add a `SKILL.md` following the YAML front matter format in any existing skill
4. Submit a PR with a short description of what it does and example triggers

---

## 📬 Author

Built by [@Platypeak](https://github.com/Platypeak) — PHP & web dev, agentic AI workflows enthusiast.

---

## ⭐ Show Some Love

If this saved you time, drop a ⭐ on the repo — it helps others discover it!
