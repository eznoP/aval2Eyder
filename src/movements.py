
import json
from datetime import datetime

def add_movement():       
    # LÊ O ARQUIVO (OU CRIA UM NOVO) , PEGA DATA E HORA ATUAIS , PEGA A DESCRIÇÃO DA MOVIMENTAÇÃO , ADICIONA NA LISTA E SALVA DE VOLTA NO ARQUIVO.
    
    try :
        f = open('movements.json', 'r', encoding='utf-8')
        movements = json.load(f)
        f.close()
    except:
        print("Arquivo não existe, criando um novo...")
        movements = []

    data = str(datetime.now())
    descricao = input("Descrição da movimentação: ")

    movimento = {"date": data, "description": descricao}

    movements.append(movimento)

    f = open('movements.json', 'w', encoding='utf-8')
    json.dump(movements, f)
    f.close()

    print("Movimentação registrada com sucesso!")
