from files import load_data, save_data

FILENAME = 'inputs.json'

def add_input():
    inputs = load_data(FILENAME)
    item = {
        "id": input("ID do insumo: "),
        "name": input("Nome: "),
        "quantity": float(input("Quantidade: ")),
        "unit": input("Unidade: "),
        "category": input("Categoria: ")
    }
    inputs.append(item)
    save_data(FILENAME, inputs)
    print("✅ Insumo cadastrado!")

def update_stock():
    inputs = load_data(FILENAME)
    item_id = input("ID do insumo: ")
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
