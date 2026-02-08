from flask import Blueprint, request, jsonify
from services.weather_service import get_weather

weather_bp = Blueprint("weather", __name__)

@weather_bp.route("/weather", methods=["POST"])
def weather():
    data = request.json
    city = data.get("city")
    return jsonify(get_weather(city))
