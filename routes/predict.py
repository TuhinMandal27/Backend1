# from flask import Blueprint, request, jsonify
# from services.predict_service import predict_disease

# predict_bp = Blueprint("predict", __name__)

# @predict_bp.route("/predict", methods=["POST"])
# def predict():
#     if "image" not in request.files:
#         return jsonify({"error": "No image uploaded"}), 400
#     image = request.files["image"]
#     result = predict_disease(image)

#     return jsonify(result)
