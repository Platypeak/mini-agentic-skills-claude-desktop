# 🤖 Mini Agentic Skills — Claude Desktop

> **Plug-and-play skill files that make Claude Desktop smarter, faster, and more agentic.**

![Claude Desktop](https://img.shields.io/badge/Claude-Desktop-blueviolet?style=for-the-badge&logo=anthropic)
![Skills](https://img.shields.io/badge/Skills-Growing-brightgreen?style=for-the-badge)
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

> More skills coming soon. Star ⭐ the repo to stay updated!

---

## 🚀 How to Use

### Step 1 — Clone or download a skill

```bash
git clone https://github.com/Platypeak/mini-agentic-skills-claude-desktop.git
```

### Step 2 — Point Claude Desktop to the skills folder

In your `claude_desktop_config.json`, add the skills directory path so Claude can read them at runtime. Each `SKILL.md` file is auto-detected and loaded when relevant.

### Step 3 — Just talk to Claude

Once a skill is loaded, Claude will automatically trigger it when your message matches the skill's use case. No commands, no setup — just natural conversation.

---

## 🧠 How Skills Work

Each skill is a `SKILL.md` file inside its own folder. It contains:

- **A YAML front matter block** — tells Claude *when* to trigger the skill (description + name)
- **A step-by-step workflow** — tells Claude *how* to execute the task
- **Rules & edge cases** — guardrails to keep Claude precise and safe

```
mini-agentic-skills-claude-desktop/
│
├── project-settlement/
│   └── SKILL.md        ← Handles uploaded ZIP project edits
│
├── your-skill-here/
│   └── SKILL.md
│
└── README.md
```

---

## 🤝 Contributing

Got a skill idea? PRs are welcome!

1. Fork the repo
2. Create a folder with your skill name
3. Add a `SKILL.md` following the format in any existing skill
4. Submit a PR with a short description of what it does

---

## 📬 Author

Built by [@Platypeak](https://github.com/Platypeak) — PHP & web dev, agentic AI workflows enthusiast.

---

## ⭐ Show Some Love

If this saved you time, drop a ⭐ on the repo — it helps others discover it!
