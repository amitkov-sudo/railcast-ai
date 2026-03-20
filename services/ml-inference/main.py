import os

from fastapi import FastAPI

from model_loader import ModelLoader
from predict import InferenceRequest, InferenceResponse

app = FastAPI(
    title="railcast-ai Inference Service",
    description="Dedicated model inference API for delay predictions.",
    version="0.1.0",
)

loader = ModelLoader(model_path=os.getenv("MODEL_PATH", "./ml/models/latest_model.pkl"))


@app.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "healthy"}


@app.post("/predict", response_model=InferenceResponse)
def predict(payload: InferenceRequest) -> InferenceResponse:
    prediction = loader.predict_delay_minutes(payload.model_dump())
    version = loader.model["version"] if loader.model else "unknown"
    return InferenceResponse(predicted_delay_minutes=prediction, model_version=version)
