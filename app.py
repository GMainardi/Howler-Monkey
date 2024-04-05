import os
import shutil
import tempfile
from fastapi import HTTPException
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse

from src.HowlerMonkey.config.configuration import ConfigurationManager
from src.HowlerMonkey.components.prediction import Prediction

config_manager = ConfigurationManager()


app = FastAPI()
predictor = Prediction(config_manager.get_prediction_config())


@app.get("/")
async def home():
    return {"message": "YOLO Model API is running. Use /process-video/ to process videos and /train to re-train the model."}



@app.get("/train/")
async def train_model():
    try:
        os.system("dvc repro")
        return {"message": "Model training initiated successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/process-video/")
async def process_video(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_file:
        shutil.copyfileobj(file.file, temp_file)
        temp_file_path = temp_file.name

    processed_video_path = predictor.predict(temp_file_path)

    return FileResponse(processed_video_path, media_type="video/mp4", filename="processed_video.mp4")



