from pathlib import Path


def run(output_dir: str = "data/raw") -> Path:
    target = Path(output_dir) / "bart_tripupdates_placeholder.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("Replace with BART trip updates collection logic.\n", encoding="utf-8")
    return target


if __name__ == "__main__":
    print(run())
