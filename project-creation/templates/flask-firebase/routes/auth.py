from flask import Blueprint, request, jsonify
from firebase_admin import auth
from functools import wraps

auth_bp = Blueprint("auth", __name__)

def verify_token(f):
    """Decorator: verifies Firebase ID token in Authorization header."""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization", "").replace("Bearer ", "")
        if not token:
            return jsonify({"error": "Missing token"}), 401
        try:
            decoded = auth.verify_id_token(token)
            request.uid = decoded["uid"]
            request.user = decoded
        except Exception as e:
            return jsonify({"error": "Invalid token", "detail": str(e)}), 401
        return f(*args, **kwargs)
    return decorated

@auth_bp.route("/verify", methods=["POST"])
@verify_token
def verify():
    return jsonify({"uid": request.uid, "status": "authenticated"}), 200
