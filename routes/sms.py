from flask import Blueprint, request, jsonify
from services.sms_service import send_sms

sms_bp = Blueprint("sms", __name__)

@sms_bp.route("/sms", methods=["POST"])
def sms():
    data = request.json
    phone = data.get("phone")
    message = data.get("message")
    return jsonify(send_sms(phone, message))
