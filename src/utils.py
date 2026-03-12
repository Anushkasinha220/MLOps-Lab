import json
from pathlib import Path

def ensure_directory(path):
    Path(path).mkdir(parents=True, exist_ok=True)

def save_json(data, filepath):
    ensure_directory(Path(filepath).parent)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

def load_json(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

if __name__ == "__main__":
    print("Utilities loaded successfully")