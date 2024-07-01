import os
import cv2
from ultralytics import YOLO


"Train19 was best till Now , But not detecting my cities"
# Load the model with CUDA support
model = YOLO('runs/detect/train21/weights/best.pt').to('cuda')

# Input and output directories
input_dir = 'C:\\Users\\omkis\\Downloads\\MillionLords\\Train\\Test'
output_dir = 'C:\\Users\\omkis\\Downloads\\MillionLords\\Train\\Output'

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Iterate over images in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Read the image
        img_path = os.path.join(input_dir, filename)
        img = cv2.imread(img_path)

        # Run prediction on the image
        results = model.predict(img,conf=0.5)

        # Iterate over the results
        for result in results:
            boxes = result.boxes.cpu().numpy()  # Get boxes on CPU in numpy format
            for box in boxes:  # Iterate over boxes
                r = box.xyxy[0].astype(int)  # Get corner points as int
                class_id = int(box.cls[0])  # Get class ID
                class_name = model.names[class_id]  # Get class name using the class ID
                # print(f"Class: {class_name}, Box: {r}")  # Print class name and box coordinates
                cv2.rectangle(img, (r[0], r[1]), (r[2], r[3]), (0, 255, 0), 2)  # Draw boxes on the image
                cv2.putText(img, class_name, (r[0], r[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)  # Put label on the image

        # Save the labeled image
        output_path = os.path.join(output_dir, filename)
        cv2.imwrite(output_path, img)
        print(f"Labeled image saved: {output_path}")

print("All images processed.")
