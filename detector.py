from ultralytics import YOLO
import torch

class Detector:
    def __init__(self, model_path='models/yolov8m.pt', use_cuda=True):
        self.device = 'cuda' if use_cuda and torch.cuda.is_available() else 'cpu'
        self.model = YOLO(model_path).to(self.device)
        self.names = self.model.names

    def detect(self, frame):
        results = self.model.track(source=frame, persist=True, conf=0.5, tracker='bytetrack.yaml')
        return results[0]
