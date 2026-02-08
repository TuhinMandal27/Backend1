from flask import Blueprint, request, jsonify
from services.crop_service import recommend_crop

crop_bp = Blueprint("crop", __name__)

@crop_bp.route("/crop", methods=["POST"])
def crop():
    data = request.json
    return jsonify(recommend_crop(data))
