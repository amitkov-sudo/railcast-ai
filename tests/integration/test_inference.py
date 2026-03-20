import importlib.util
from pathlib import Path
import sys

from fastapi.testclient import TestClient


def _load_inference_app():
    module_path = Path("services/ml-inference/main.py").resolve()
    sys.path.insert(0, str(module_path.parent))
    spec = importlib.util.spec_from_file_location("ml_inference_main", module_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.app


def test_predict_endpoint() -> None:
    app = _load_inference_app()
    client = TestClient(app)
    response = client.post("/predict", json={"train_id": "A123", "current_delay_minutes": 4})
    assert response.status_code == 200
    body = response.json()
    assert "predicted_delay_minutes" in body
