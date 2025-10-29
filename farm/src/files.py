import json

DATA_PATH = '../data/'  # CAMINHO DA PASTA ONDE FICA O ARQUIVO

def load_data(filename):
    caminho = DATA_PATH + filename

    # ABRE O ARQUIVO PRA LEITURA
    try:
        arquivo = open(caminho, 'r', encoding='utf-8')
        dados = json.load(arquivo)
        arquivo.close()
        return dados
    except:
        # SE O ARQUIVO NÃO EXISTIR OU ESTIVER CORROMPIDO, CRIA UM NOVO
        print('Arquivo não encontrado ou corrompido. Criando novo.')
        return []

def save_data(filename, data):
    caminho = DATA_PATH + filename

    # ABRE O ARQUIVO PARA ESRITA
    arquivo = open(caminho, 'w', encoding='utf-8')
    json.dump(data, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()
