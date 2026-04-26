# Template: PHP + MySQL Web Panel

## What This Provides
| File | Purpose |
|---|---|
| `index.php` | Entry point / dashboard |
| `config/db.php` | MySQLi connection + env config |
| `config/auth.php` | Session-based auth guard |
| `includes/header.php` | Shared HTML header + nav |
| `includes/footer.php` | Shared HTML footer |
| `assets/css/style.css` | Base CSS (can swap for Bootstrap) |
| `assets/js/main.js` | Base JS |
| `api/` | Placeholder folder for AJAX endpoints |
| `.htaccess` | Clean URLs + security headers |
| `.env.example` | DB credentials template |
| `.gitignore` | PHP + env ignores |
| `README.md` | Setup instructions |

## Placeholders
| Placeholder | Replaced With |
|---|---|
| `{{PROJECT_NAME}}` | Panel title / page title |
| `{{DESCRIPTION}}` | One-line description |
| `{{AUTHOR}}` | Developer name |
| `{{DB_NAME}}` | MySQL database name |

## Manual Steps After Generation
1. Create a MySQL database matching `{{DB_NAME}}`
2. Copy `.env.example` → `.env` and fill in DB credentials
3. Import any SQL schema files if generated
4. Deploy to Apache/Nginx with PHP 8.x
5. Ensure `mod_rewrite` is enabled for `.htaccess` to work
