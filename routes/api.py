from flask import Blueprint, request, jsonify
from services.logic import process_data

api_bp = Blueprint("api", __name__)

@api_bp.route("/submit", methods=["POST"])
def submit_data():
    data = request.json
    result = process_data(data)
    return jsonify(result)


@api_bp.route("/get-data", methods=["GET"])
def get_data():
    return jsonify({
        "message": "Hello from Flask backend",
        "status": "success"
    })
