from pydantic import BaseModel, Field


class InferenceRequest(BaseModel):
    train_id: str = Field(...)
    current_delay_minutes: float = Field(default=0.0)


class InferenceResponse(BaseModel):
    predicted_delay_minutes: float
    model_version: str
