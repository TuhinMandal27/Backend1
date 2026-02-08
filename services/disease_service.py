import tensorflow as tf
import numpy as np
from PIL import Image

model = tf.keras.models.load_model("model/plant_disease_model.h5")

def preprocess(img):
    img = img.resize((224, 224))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    return img

def predict_disease(image_file):
    img = Image.open(image_file).convert("RGB")
    processed = preprocess(img)

    prediction = model.predict(processed)
    index = np.argmax(prediction)
    confidence = float(np.max(prediction))

    classes = ["Healthy", "Disease A", "Disease B"]  # update this

    return {
        "disease": classes[index],
        "confidence": round(confidence * 100, 2)
    }
