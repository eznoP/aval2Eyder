from utilitys import clear, return_to_menu  
from files import load_data, save_data

FILENAME = 'animals.json'

def add_animal():
    
    animals = load_data(FILENAME) 
    
    print('\n==== ADICIONAR NOVO ANIMAL ====')
    try:
        animal = {                                             # PROCESSO DE ADICIONAR ANIMAL
            "id": int(input("ID do animal (0001): ")),
            "species": input("Espécie (ex: “bovino”, “caprino”, “aves”, “suíno”): "),
            "age": float(input("Idade em meses: ")),
            "weight": float(input("Peso em kg: ")),
            "status": "active"
        }
        animals.append(animal)         # ADICIONA O NOVO ANIMAL NA LISTA DE ANIMAIS                                                               
        save_data(FILENAME, animals)   # SALVA O NOVO ANIMAL NA LISTA
        clear()
        print("✅ Animal cadastrado com sucesso!")
        return_to_menu()
    
    except ValueError:
        clear()
        print("❌ Erro: digite apenas números em ID, idade e peso.")
        return_to_menu()

def list_animals():                 # FUNÇÃO QUE VERIFICA SE EXISTE ALGUM ANIMAL JÁ CADASTRADO, CASO NÃO HAJA NENHUM ARQUIVO COM A LISTA DE ANIMAIS, 
    animals = load_data(FILENAME)   # SERÁ CRIADO UM NOVO AQUIVO PARA QUE A LISTA DE ANIMAIS SEJA SALVA NELE.
    
    if not animals:
        clear()
        print("Nenhum animal cadastrado.")
        return_to_menu()
        return
    
    for a in animals:
        print(f"{a['id']} - {a['species']} - {a['age']} anos - {a['weight']} kg - {a['status']}")
