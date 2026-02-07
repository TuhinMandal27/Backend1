def process_data(data):
    name = data.get("name", "User")
    return {
        "response": f"Hello {name}, data received successfully!",
        "received_data": data
    }
