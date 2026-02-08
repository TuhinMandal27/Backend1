def process_voice(text):
    if not text:
        return {"error": "No voice text received"}

    # simple NLP logic
    text = text.lower()

    if "weather" in text:
        return {"reply": "Please go to weather section"}
    elif "disease" in text:
        return {"reply": "Upload leaf image to detect disease"}
    elif "crop" in text:
        return {"reply": "Go to crop recommendation page"}

    return {"reply": f"You said: {text}"}
