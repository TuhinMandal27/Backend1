def recommend_crop(data):
    soil = data.get("soil")
    season = data.get("season")

    if soil == "loamy" and season == "summer":
        return {"crop": "Rice"}
    return {"crop": "Wheat"}
