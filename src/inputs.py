from files import load_data, save_data
from utilitys import clear

FILENAME = "inputs.json"

def add_input():                                           # ADICIONAR NOVO INSUMO
    print('\n==== ADICIONAR NOVO INSUMO ====')
    insumo = {}
       
    insumo["id"] = input("Digite o ID do insumo (ex: A001): ")
    insumo["name"] = input("Nome do insumo (Ração bovina, semente de milho, adubo NPK 20-10=10): ")
    try:
        insumo["quantity"] = float(input("Quantidade disponível: "))
    except ValueError:
        print("Quantidade inválida. Use um número (ex: 12.5).")
        return
    insumo["unit"] = input("Unidade de medida (kg, L, saco, dose): ")
    insumo["category"] = input("Categoria (ração, semente, fertilizantes, medicina): ")
    
    data = load_data(FILENAME)                                    
    data.append(insumo)
    save_data(FILENAME, data)                                      # FUNÇÕES PARA SALVAR O NOVO INSUMO ADICIONADO
 
    clear()
    print("Insumo cadastrado com sucesso.\n")
    input("Pressione Enter para voltar. ")

def update_stock():                    # INVENTÁRIO DE INSUMOS QUE JÁ FORAM ADICIONADOS
    data = load_data(FILENAME)
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

