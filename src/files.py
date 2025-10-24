
import json
import os



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


import json         
import os          # MODÚLO QUE SERVE PARA INTERAGIR COM O SISTEMA OPERACIONAL

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data')          # CAMINHO PARA A PASTA DE DADOS

def load_data(filename):          # CARREGA OS DADOS DE UM ARQUIVO JSON
    path = os.path.join(DATA_PATH, filename)          # CAMINHO COMPLETO DO ARQUIVO
    if not os.path.exists(path):          # SE O ARQUIVO NÃO EXISTIR, RETORNA UMA LISTA VAZIA   
        return []
    try:
        with open(path, 'r', encoding='utf-8') as file:          # ABRE O ARQUIVO PARA LEITURA
            return json.load(file)          # CARREGA E RETORNA OS DADOS DO ARQUIVO
    except json.JSONDecodeError:           # TRATA O ERRO CASO O ARQUIVO ESTEJA VAZIO OU CORROMPIDO
        print(f"Aviso: {filename} estava vazio ou corrompido. Criando novo.")
        return []

def save_data(filename, data):          # SALVA OS DADOS EM UM ARQUIVO JSON
    path = os.path.join(DATA_PATH, filename)         # CAMINHO COMPLETO DO ARQUIVO
    with open(path, 'w', encoding='utf-8') as file:          # ABRE O ARQUIVO PARA ESCRITA
        json.dump(data, file, indent=4, ensure_ascii=False)          # SALVA OS DADOS NO ARQUIVO COM FORMATAÇÃO

