# Template: Flask + Firebase

## What This Provides
| File | Purpose |
|---|---|
| `app.py` | Flask app entry point, route registration |
| `config.py` | Firebase Admin SDK init, env config |
| `requirements.txt` | All Python dependencies |
| `.env.example` | Environment variable template |
| `.gitignore` | Python + Firebase ignores |
| `README.md` | Setup and run instructions |
| `routes/__init__.py` | Routes package init |
| `routes/auth.py` | Firebase Auth token verification middleware |
| `models/__init__.py` | Models package init |
| `models/base.py` | Firestore base model helper |
| `utils/__init__.py` | Utils package init |
| `utils/response.py` | Standardized JSON response helpers |
| `firebase-adminsdk.json.example` | Placeholder for service account key |

## Placeholders
| Placeholder | Replaced With |
|---|---|
| `{{PROJECT_NAME}}` | Python package / folder name |
| `{{DESCRIPTION}}` | One-line app description |
| `{{AUTHOR}}` | Developer name |
| `{{FIREBASE_PROJECT_ID}}` | Firebase project ID |

## Manual Steps After Generation
1. Download Firebase Admin SDK JSON from Firebase Console → Project Settings → Service Accounts
2. Rename it to `firebase-adminsdk.json` and place it in the project root
3. Copy `.env.example` → `.env` and fill in your values
4. Run `pip install -r requirements.txt`
5. Run `python app.py`
