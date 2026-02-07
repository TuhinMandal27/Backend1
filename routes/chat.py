from flask import Blueprint, request, jsonify
from services.chat_service import get_reply

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.json
    reply = get_reply(data)
    return jsonify(reply)
