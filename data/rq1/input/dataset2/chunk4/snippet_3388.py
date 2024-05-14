#Source: https://stackoverflow.com/questions/77344941/typeerror-expected-str-bytes-or-os-pathlike-object-not-nonetype-yolo
from ultralytics import YOLO

model = YOLO('yolov8n-cls.pt')

model.train(data='./training_dataset', epochs=1, imgsz=64)