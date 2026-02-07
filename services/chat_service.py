def get_reply(data):
    msg = data.get("message", "").lower()
    lang = data.get("language", "en")

    if "rice" in msg or "धान" in msg or "ধান" in msg:
        return {"reply": "For rice crops, ensure proper drainage and nitrogen balance."}

    if "weather" in msg or "rain" in msg or "बर्षा" in msg:
        return {"reply": "Heavy rain expected. Avoid fertilizer application today."}

    if "disease" in msg:
        return {"reply": "Please describe symptoms or upload a photo."}

    return {"reply": "Please ask about crops, weather, or disease."}
