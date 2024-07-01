# YOLOv8 Object Detection Project

This project leverages the YOLOv8 model for object detection, enabling users to train custom models, make predictions on images and videos, and perform utility tasks such as moving the cursor and extracting text from the screen. The scripts are designed to be run with minimal configuration and can be easily adapted to different use cases.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
  - [Training](#training)
  - [Prediction on Images](#prediction-on-images)
  - [Prediction on Videos](#prediction-on-videos)
  - [Move Cursor and Extract Text](#move-cursor-and-extract-text)
- [Dependencies](#dependencies)

## Introduction

This project is designed to facilitate object detection tasks using the YOLOv8 model. It includes scripts for training the model, making predictions on both images and videos, and a utility script for moving the cursor and extracting text from the screen. The goal is to provide a comprehensive toolkit for developing and deploying object detection applications.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Training

To train the YOLOv8 model, run the `train.py` script. Make sure you have the configuration files (`yolov8s.yaml` and `config.yaml`) properly set up.

```sh
python train.py
```

### Prediction on Images
To run predictions on images, use the predict.py script. Specify the input and output directories in the script.

```sh
python predict.py
```
### Prediction on Videos
To run predictions on videos, use the predict_video.py script. Set the video_path to the path of your input video.

```sh
python predict_video.py
```
### Move Cursor and Extract Text
The movecursor.py script allows you to move the cursor randomly within a specified range and extract text from a screen region.

```sh
python movecursor.py
```
### Dependencies
Python 3.8+
ultralytics
cv2 (OpenCV)
pytesseract
pyautogui
numpy
easyocr
To install dependencies, run:

```sh
pip install -r requirements.txt
```
