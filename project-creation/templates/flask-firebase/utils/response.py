from flask import jsonify

def success(data=None, message="Success", status=200):
    return jsonify({"status": "success", "message": message, "data": data}), status

def error(message="An error occurred", status=400, detail=None):
    payload = {"status": "error", "message": message}
    if detail:
        payload["detail"] = detail
    return jsonify(payload), status
