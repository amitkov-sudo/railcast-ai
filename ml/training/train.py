from pathlib import Path


def train_model() -> Path:
    """Placeholder training entrypoint."""
    model_path = Path("ml/models/latest_model.pkl")
    model_path.parent.mkdir(parents=True, exist_ok=True)
    model_path.write_text("Replace with serialized model artifact.\n", encoding="utf-8")
    return model_path


if __name__ == "__main__":
    print(train_model())
