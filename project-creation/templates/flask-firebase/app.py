from flask import Flask
from config import init_firebase
from routes import register_routes

app = Flask(__name__)

# Initialize Firebase Admin SDK
init_firebase()

# Register all route blueprints
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
