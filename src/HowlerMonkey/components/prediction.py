import cv2
from pathlib import Path
from ultralytics import YOLO

from HowlerMonkey.utils.common import get_latest_model
from HowlerMonkey.entity.config_entity import PredictionConfig


class Prediction:
    def __init__(self, config: PredictionConfig):
        self.config = config


    @staticmethod
    def load_model(model_path: Path):
        return YOLO(get_latest_model(model_path))
    
    def open_video(self, video_path: Path):
        return cv2.VideoCapture(str(video_path))
    
    def load_video_writer(self, cap: cv2.VideoCapture) -> cv2.VideoWriter:
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        return cv2.VideoWriter(self.config.prediction_output, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))
    
    def predict(self, video_path: Path) -> str:
        
        model = self.load_model(self.config.model_path)
        cap = self.open_video(video_path)
        out = self.load_video_writer(cap)

        while cap.isOpened():

            ret, frame = cap.read()

            if not ret:
                break

            result = model.track(frame, persist=True)

            out.write(result[0].plot())

        cap.release()
        out.release()
        cv2.destroyAllWindows()

        return self.config.prediction_output
