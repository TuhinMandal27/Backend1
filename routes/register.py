from flask import Blueprint, request, jsonify
from services.register_service import save_user

register_bp = Blueprint("register", __name__)

@register_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    response = save_user(data)
    return jsonify(response)
