from files import load_data, save_data   # FUNÇÕES PARA CARREGAR E SALVAR DADOS

FILENAME = 'inputs.json'  

def add_input():
    inputs = load_data(FILENAME)
    item = {                            # INICIO DE CADASTRO DO NOVO INSUMO
        "id": input("ID do insumo: "),
        "name": input("Nome (ex: “Ração bovina”, “Semente de milho”, “Adubo NPK 20-10-10”):  "),
        "quantity": float(input("Quantidade em kilogramas:   ")),
        "unit": input("Unidade em sacos:   "),
        "category": input("Categoria (ração, semente, fertilizante, medicina): ")
    }
    inputs.append(item)
    save_data(FILENAME, inputs)
    print("✅ Insumo cadastrado!")

def update_stock():                # FUNÇÃO PARA GERENCIAR INSUMOS 
    inputs = load_data(FILENAME)   # PERMITE DIZER A QUANTIDADE DE INSUMO RETIRADA DO ESTOQUE
    item_id = input("ID do insumo: ") # SALVA AS RETIRADAS
    for i in inputs:
        if i['id'] == item_id:
            try:
                amount = float(input("Quantidade (negativo = saída): "))
                if i['quantity'] + amount < 0:
                    print("❌ Saída maior que estoque disponível!")
                    return
                i['quantity'] += amount
                save_data(FILENAME, inputs)
                print("✅ Estoque atualizado!")
                return
            except ValueError:
                print("❌ Valor inválido.")
                return
    print("❌ Insumo não encontrado.")
