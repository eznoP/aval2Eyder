import re   # EXPRESSÕES REGULARES PARA FAZER O FORMATO DE ID (A001)
from files import load_data, save_data #Funçoes para carregar e salvar dados 
from utilitys import clear, return_to_menu #Funçao limpar tela e voltar pro menu

FILENAME = "inputs.json" #Onde os arquivos vao ficar armazenados            

def add_input():                                           # ADICIONAR NOVO INSUMO
   
    data = load_data(FILENAME)                                    
    
    user_choose = (input(">>> Deseja realmente adicionar um novo insumo? (Pressione Enter para continuar ou 0 para voltar ao menu): ")) #Confirmação de opção para o usuario 
    clear()
    if user_choose == "0":
        clear()
        return

    print('\n==== ADICIONAR NOVO INSUMO ====\n')

       
    ID = input("> Digite o ID do insumo (ex: A001): ")
    if not re.fullmatch(r"[A-Za-z]\d{3}", ID): 
        print(f"ID ({ID}) inválido. Use apenas uma letra seguida de três números (ex: A001).")
        return_to_menu()
        return
    
    name = input("> Nome do insumo (Ração bovina, semente de milho, adubo NPK 20-10=10): ")
    
    try:
        quantity = float(input("> Quantidade disponível (ex: 10.0): "))
    except ValueError:
        print(f"Quantidade ({quantity}) inválida. Use um número seguido de .(ponto) e outro número. (ex: 10.0).")
        return
    
    unit = input("> Unidade de medida (Kg, L, saco, dose): ")
    if unit.lower() not in ["kg", "l", "aco", "dose"]:
        print(f"Unidade ({unit}) inválida. Use apenas 'kg', 'L', 'saco' ou 'dose'.")
        return
    
    category = input("> Categoria (ração, semente, fertilizantes, medicina): ")
    if category.lower() not in ["ração", "semente", "fertilizantes", "medicina"]:
        print(f"Categoria ({category}) inválida. Use apenas 'ração', 'semente', 'fertilizantes' ou 'medicina'.")
        return
    
    
    insumo = {
        "id": ID,
        "name": name,
        "quantity": quantity,
        "unit": unit,
        "category": category
    }
    
    
    data.append(insumo)
    save_data(FILENAME, data)                                      # FUNÇÕES PARA SALVAR O NOVO INSUMO ADICIONADO
 
    clear()
    print("Insumo cadastrado com sucesso.\n")
    return_to_menu()

def update_stock():                    # INVENTÁRIO DE INSUMOS QUE JÁ FORAM ADICIONADOS
    data = load_data(FILENAME)
    
    if not data:
        print("Nenhum insumo cadastrado ainda.\n\n")
        return_to_menu()
        return

    print("\n--- LISTA DE INSUMOS ---")
    
    for insumo in data:
    
        print(f"ID: {insumo['id']}")
        print(f"Nome: {insumo['name']}")
        print(f"Quantidade: {insumo['quantity']} {insumo['unit']}")
        print(f"Categoria: {insumo['category']}")
        print("-----------------------------\n\n")
        return_to_menu()


