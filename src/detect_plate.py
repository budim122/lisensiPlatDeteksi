# detect_plate.py
import cv2
import numpy as np
import tensorflow as tf

def detect_plate(image_path, model_path="models/license_plate_detector.h5"):
    model = tf.keras.models.load_model(model_path)
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (224, 224)) / 255.0
    image = np.expand_dims(image, axis=(0, -1))
    prediction = model.predict(image)
    print(f"Detection Score: {prediction}")

if __name__ == "__main__":
    detect_plate("test_image.jpg")
