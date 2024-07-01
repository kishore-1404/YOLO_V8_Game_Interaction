from ultralytics import YOLO
import multiprocessing

if __name__ == '__main__':
    multiprocessing.freeze_support()
    
    model = YOLO("yolov8s.yaml").to('cuda')

    results = model.train(data="config.yaml", epochs=300,augment= True)
