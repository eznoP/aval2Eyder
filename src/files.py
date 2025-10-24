
import json    

def load_data(arquivo):
    # LÊ OS ARQUIVOS E DESENVOLVE OS DADOS , SE O ARQUIVO NÃO EXISTIR , DEVOLVE UMA LISTA VAZIA.

    try:
        f = open(arquivo, 'r', encoding='utf-8')
        dados = json.load(f)
        f.close()
        return dados
    except:
        print("estava vazio ou corrompido. Criando novo.")
        return []

def save_data(arquivo, dados):
    # PEGA A VARIÁVEL DE DADOS E SALVA DENTRO DO ARQUIVO.

    f = open(arquivo, 'w', encoding='utf-8')
    json.dump(dados, f)
    f.close()
