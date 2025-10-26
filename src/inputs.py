import json
from files import load_data, save_data
FILENAME = "inputs.json"

def register_input():
    insumo = {}
    insumo["id"] = input("Digite o ID do insumo (ex: I001): ")
    insumo["name"] = input("Nome do insumo: ")
    insumo["quantity"] = float(input("Quantidade disponível: "))
    insumo["unit"] = input("Unidade de medida (kg, L, saco, dose): ")
    insumo["category"] = input("Categoria (feed, seed, fertilizer, medicine): ")

    data = load_data()
    data.append(insumo)
    save_data(data)

    print("Insumo cadastrado.\n")


def list_input():
    data = load_data()
    if not data:
        print("Nenhum insumo cadastrado ainda.")
        return

    print("\n--- LISTA DE INSUMOS ---")
    for insumo in data:
        print(f"ID: {insumo['id']}")
        print(f"Nome: {insumo['name']}")
        print(f"Quantidade: {insumo['quantity']} {insumo['unit']}")
        print(f"Categoria: {insumo['category']}")
        print("-----------------------------")
    print()

def main():
    while True:
        print("1 - Cadastrar novo insumo")
        print("2 - Listar insumos")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            register_input()
        elif opcao == "2":
            list_input()
        elif opcao == "3":
            break
        else:
            print("Opção inválida.\n")

main()
