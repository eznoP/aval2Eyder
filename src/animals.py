from files import load_data, save_data

FILENAME = 'animals.json'

def add_animal():
    animals = load_data(FILENAME) 
    try:
        animal = {                                                                             # PROCESSO DE ADICIONAR ANIMAL
            "id": int(input("ID do animal: ")),
            "species": input("Espécie (ex: “bovino”, “caprino”, “aves”, “suíno”): "),
            "age": float(input("Idade: ")),
            "weight": float(input("Peso: ")),
            "status": "active"
        }
        animals.append(animal)       # ADICIONA O NOVO ANIMAL NA LISTA DE ANIMAIS                                                               
        save_data(FILENAME, animals)   # SALVA O NOVO ANIMAL NA LISTA
        print("✅ Animal cadastrado com sucesso!")
    except ValueError:
        print("❌ Erro: digite apenas números em ID, idade e peso.")

def list_animals():             # FUNÇÃO QUE VERIFICA SE EXISTE ALGUM ANIMAL JÁ CADASTRADO, CASO NÃO HAJA NENHUM ARQUIVO COM A LISTA DE ANIMAIS, 
    animals = load_data(FILENAME) # SERÁ CRIADO UM NOVO AQUIVO PARA QUE A LISTA DE ANIMAIS SEJA SALVA NELE.
    if not animals:
        print("Nenhum animal cadastrado.")
        return
    for a in animals:
        print(f"{a['id']} - {a['species']} - {a['age']} anos - {a['weight']} kg - {a['status']}")
