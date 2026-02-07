def save_user(data):
    name = data.get("name")
    phone = data.get("phone")
    language = data.get("language")
    district = data.get("district")

    if not phone:
        return {"success": False, "message": "Phone number required"}

    # For now just log (later DB)
    print("New Registration:", name, phone, language, district)

    return {
        "success": True,
        "message": "Registration successful"
    }
