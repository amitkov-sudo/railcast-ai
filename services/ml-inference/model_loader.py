from pathlib import Path


class ModelLoader:
    def __init__(self, model_path: str) -> None:
        self.model_path = Path(model_path)
        self.model = None

    def load(self) -> None:
        # Placeholder: replace with real deserialization logic (joblib/pickle/onnx).
        self.model = {"name": "baseline-delay-model", "version": "0.1.0"}

    def predict_delay_minutes(self, features: dict) -> float:
        if self.model is None:
            self.load()
        # Placeholder deterministic baseline.
        return float(features.get("current_delay_minutes", 0.0))
