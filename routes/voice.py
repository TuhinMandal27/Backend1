from flask import Blueprint, request, jsonify
from services.voice_service import process_voice

voice_bp = Blueprint("voice", __name__)

@voice_bp.route("/voice", methods=["POST"])
def voice():
    data = request.json
    text = data.get("text")
    return jsonify(process_voice(text))
