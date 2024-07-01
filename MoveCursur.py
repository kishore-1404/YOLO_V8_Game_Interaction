import pytesseract
import pyautogui
import time
import random
import cv2
import numpy as np
import easyocr
# Install pytesseract if not already installed
# pip install pytesseract
x_numbers = list(range(-600, 601, 50))
y_numbers = list(range(-400, 400, 50))
# Set the path to the Tesseract executable (change this according to your system)
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\omkis\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def preprocess_image(image):
    # Convert the image to grayscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(grayscale, (5, 5), 0)
    
    # Apply adaptive thresholding to binarize the image
    thresholded = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    
    return thresholded
def extract_text_from_screen(rect_coords):
    # Take a screenshot of the screen
    screenshot = pyautogui.screenshot()
    
    # Convert the screenshot to an OpenCV image format
    screenshot_cv = np.array(screenshot)
    screenshot_cv = cv2.cvtColor(screenshot_cv, cv2.COLOR_RGB2BGR)

    # Extract the rectangular region
    x, y, width, height = rect_coords["x"], rect_coords["y"], rect_coords["width"], rect_coords["height"]
    region = screenshot_cv[y:y+height, x:x+width]
    # Preprocess the region
    preprocessed_region = preprocess_image(region)
    # cv2.imshow("Preprocessed Region", preprocessed_region)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # Initialize EasyOCR reader
    reader = easyocr.Reader(['en'])

    # Perform OCR (Optical Character Recognition) on the preprocessed region
    # result = reader.readtext(region)
    allowlist = ["-","_",";","1","2","3","4","5","6","7","8","9","0"]
    result = reader.readtext(region, mag_ratio=2.0, allowlist=allowlist) 
    # result = reader.readtext(region, allowlist ='0123456789;-')
    _text = pytesseract.image_to_string(preprocessed_region, config='--psm 6 --oem 3')
    print(_text.strip())

    # Extract text from the result
    extracted_text = ""
    for detection in result:
        extracted_text += detection[1] + " "

    return extracted_text.strip()


def drag():
    # Starting coordinates (where to click and hold)
    x_start, y_start = 1920//2, 1080//2  # Replace with your desired coordinates
    pyautogui.moveTo(x_start, y_start)
    # List of integers
    
    # Randomly select one integer from the list
    x = random.choice(x_numbers)
    y = random.choice(y_numbers)
    print(f"({x},{y})")
    pyautogui.dragRel(x,y,2,button='left')

# Rectangular coordinates

# time.sleep(3)
# # Extract text from the specified region
# extracted_text = extract_text_from_screen(rect_coords)

# print("Extracted Text:")
# print(extracted_text)

if __name__ == "__main__":
    "If full Screen"
    rect_coords = {"x": 880, "y": 195, "width": 150, "height": 50}
    "If not"
    # rect_coords = {"x":870,"y":220,"width":135,"height":50}
    time.sleep(3)
    pyautogui.press('f11')
    time.sleep(3)
    for i in range(1):
        extracted_text = extract_text_from_screen(rect_coords)
        # drag()
        time.sleep(0.2)
        print("Extracted Text: "+ extracted_text)

