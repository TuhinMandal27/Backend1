from flask import Blueprint, request, jsonify
from services.disease_service import predict_disease

disease_bp = Blueprint("disease", __name__)

@disease_bp.route("/disease", methods=["POST"])
def disease():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files["image"]
    return jsonify(predict_disease(image))
