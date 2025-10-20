import json
import os

DATA_PATH = 'data'

def load_data(filename):
    filepath = os.path.join(DATA_PATH, filename)
    if not os.path.exists(filepath):
        save_data(filename, [])
        with open(filepath, 'r', encoding='utf-8') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []

def save_data(filename, data):
    filepath = os.path.join(DATA_PATH, filename)
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, inden=4, ensure_ascii=False)