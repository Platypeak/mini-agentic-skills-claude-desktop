# Template: PyQt6 Desktop App

## What This Provides
| File | Purpose |
|---|---|
| `main.py` | App entry point, QApplication init |
| `requirements.txt` | PyQt6 + common dependencies |
| `.gitignore` | Python ignores |
| `README.md` | Setup and run instructions |
| `ui/main_window.py` | Main QMainWindow subclass |
| `ui/styles.qss` | Qt stylesheet for consistent theming |
| `core/__init__.py` | Core logic package |
| `core/database.py` | SQLite DB manager (optional, ready to use) |
| `assets/` | Placeholder folder for icons/images |

## Placeholders
| Placeholder | Replaced With |
|---|---|
| `{{PROJECT_NAME}}` | App name shown in title bar |
| `{{DESCRIPTION}}` | One-line app description |
| `{{AUTHOR}}` | Developer name |
| `{{WINDOW_WIDTH}}` | Default window width (e.g. 1200) |
| `{{WINDOW_HEIGHT}}` | Default window height (e.g. 800) |

## Manual Steps After Generation
1. `pip install -r requirements.txt`
2. `python main.py`
3. Replace `assets/` placeholder with real icons as needed
