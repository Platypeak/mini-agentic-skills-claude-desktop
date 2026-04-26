# {{PROJECT_NAME}}

{{DESCRIPTION}}

**Author:** {{AUTHOR}}  
**Stack:** Python · Flask · Firebase Firestore · Firebase Auth

---

## Setup

### 1. Clone and install
```bash
pip install -r requirements.txt
```

### 2. Firebase service account
- Go to Firebase Console → Project Settings → Service Accounts
- Click **Generate new private key**
- Save as `firebase-adminsdk.json` in the project root *(never commit this)*

### 3. Environment variables
```bash
cp .env.example .env
# Edit .env and fill in your values
```

### 4. Run
```bash
python app.py
```

API will be available at `http://localhost:5000`

---

## API Endpoints

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/api/auth/verify` | Bearer token | Verify Firebase ID token |

*(Add your endpoints here as you build)*

---

## Project Structure
```
{{PROJECT_NAME}}/
├── app.py              # Entry point
├── config.py           # Firebase init + app config
├── requirements.txt
├── .env.example
├── routes/
│   ├── __init__.py     # Blueprint registration
│   └── auth.py         # Auth middleware + routes
├── models/
│   ├── __init__.py
│   └── base.py         # Firestore base model
└── utils/
    ├── __init__.py
    └── response.py     # JSON response helpers
```
