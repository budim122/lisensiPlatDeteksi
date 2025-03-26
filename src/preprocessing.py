# preprocessing.py
import cv2
import os
import numpy as np

def preprocess_images(input_folder="dataset", output_folder="processed_data"):
    os.makedirs(output_folder, exist_ok=True)
    for img_file in os.listdir(input_folder):
        img_path = os.path.join(input_folder, img_file)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (224, 224))
        img = img / 255.0  # Normalisasi
        save_path = os.path.join(output_folder, img_file)
        cv2.imwrite(save_path, img * 255)
    print("Preprocessing completed.")

if __name__ == "__main__":
    preprocess_images()