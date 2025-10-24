import json
import os
# JA FOI FEITO


DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data')

def load_data(filename):
    path = os.path.join(DATA_PATH, filename)
    if not os.path.exists(path):
        return []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"Aviso: {filename} estava vazio ou corrompido. Criando novo.")
        return []

def save_data(filename, data):
    path = os.path.join(DATA_PATH, filename)
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
