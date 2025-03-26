# data_collection.py
import cv2
import os

def capture_images(output_folder="dataset", num_images=100):
    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(0)
    count = 0
    while count < num_images:
        ret, frame = cap.read()
        if not ret:
            break
        img_path = os.path.join(output_folder, f"image_{count}.jpg")
        cv2.imwrite(img_path, frame)
        count += 1
        print(f"Captured {img_path}")
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_images()