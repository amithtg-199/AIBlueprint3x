import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parents[1] / "resources" / "data" / "functional_test_data.json"


def load_test_data() -> dict:
    with open(DATA_FILE, encoding="utf-8") as handle:
        return json.load(handle)
