import os
import json    

DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))          # CAMINHO ABSOLUTO PARA A PASTA DE DADOS
# Garante que a pasta de dados exista (evita criação de arquivos em CWD por acidente)
os.makedirs(DATA_PATH, exist_ok=True)

def load_data(filename):          # CARREGA OS DADOS DE UM ARQUIVO JSON
    
    path = os.path.join(DATA_PATH, filename)          # CAMINHO COMPLETO DO ARQUIVO
    # Se o arquivo não existir, cria um arquivo JSON vazio no local correto e retorna lista vazia
    if not os.path.exists(path):
        try:
            with open(path, 'w', encoding='utf-8') as f:
                json.dump([], f)
        except OSError:
            # Falha ao criar o arquivo na pasta data; retornar lista vazia para não quebrar o fluxo
            return []
        return []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:          # ABRE O ARQUIVO PARA LEITURA
            return json.load(file)          # CARREGA E RETORNA OS DADOS DO ARQUIVO
    
    except json.JSONDecodeError:           # TRATA O ERRO CASO O ARQUIVO ESTEJA VAZIO OU CORROMPIDO
        return []

   
def save_data(filename, data):                                      # SALVA OS DADOS EM UM ARQUIVO JSON
    path = os.path.join(DATA_PATH, filename)                        # CAMINHO COMPLETO DO ARQUIVO
    # Garantir que o diretório exista (precaução)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as file:                 # ABRE O ARQUIVO PARA ESCRITA
        json.dump(data, file, indent=4, ensure_ascii=False)         # SALVA OS DADOS NO ARQUIVO COM FORMATAÇÃO
