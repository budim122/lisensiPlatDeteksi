# ocr_extraction.py
import pytesseract
import cv2

def extract_text(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, config='--psm 7')
    print(f"Extracted Text: {text}")
    return text

if __name__ == "__main__":
    extract_text("detected_plate.jpg")