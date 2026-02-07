# import tensorflow as tf
# import numpy as np
# from PIL import Image
# import json

# # Load model once
# model = tf.keras.models.load_model("model/plant_disease_model.h5")

# # Load class labels
# with open("model/class_labels.json") as f:
#     class_labels = json.load(f)

# def preprocess_image(img):
#     img = img.resize((224, 224))   # change if your model uses diff size
#     img = np.array(img) / 255.0
#     img = np.expand_dims(img, axis=0)
#     return img

# def predict_disease(image_file):
#     img = Image.open(image_file).convert("RGB")
#     processed = preprocess_image(img)

#     predictions = model.predict(processed)
#     class_index = np.argmax(predictions)
#     confidence = float(np.max(predictions))

#     return {
#         "disease": class_labels[str(class_index)],
#         "confidence": round(confidence * 100, 2)
#     }
