from ultralytics import YOLO
from deepsort import DeepSort
import numpy as np

class SmartDetector:
    def __init__(self):
        self.model = YOLO("yolov8s.pt")
        self.tracker = DeepSort(max_age=30)

    def detect(self, frame):
        results = self.model(frame, classes=[0,2])
        boxes, confs, clss = [], [], []
        for r in results:
            for box in r.boxes:
                x1,y1,x2,y2 = map(int,box.xyxy[0])
                boxes.append([x1,y1,x2,y2])
                confs.append(float(box.conf))
                clss.append(int(box.cls))
        return boxes, confs, clss

    def track(self, frame, boxes, confs):
        return self.tracker.update(np.array(boxes), confs, frame)