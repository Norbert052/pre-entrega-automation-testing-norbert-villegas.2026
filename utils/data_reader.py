import csv
import json
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"


def read_csv(filename):
    path = DATA_DIR / filename
    with path.open(mode="r", encoding="utf-8") as csv_file:
        return list(csv.DictReader(csv_file))


def read_json(filename):
    path = DATA_DIR / filename
    with path.open(mode="r", encoding="utf-8") as json_file:
        return json.load(json_file)
