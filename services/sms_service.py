def send_sms(phone, message):
    if not phone or not message:
        return {"error": "Phone and message required"}

    # dummy SMS logic
    print(f"SMS sent to {phone}: {message}")

    return {
        "status": "success",
        "message": "SMS sent successfully"
    }
