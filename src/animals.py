
from files import load_data, save_data

FILENAME = "animals.json"

def load_animals():
    return load_data(FILENAME)

def save_animals(animals):
    save_data(FILENAME, animals)





def add_animal():

    animals = load_animals()
    title = print('\nCadastro de animal.')
    line = '-' * len(title)

    animal_id = int(input('Adicione o ID do animal: ').strip)
    if any(a['id'] == animal_id for a in animals):
        print('ID já cadastrado.')
        return
    
    species = input('Insira a espécie do animal (bovino, caprino, aves, etc): ').strip
    
    try:
        weight = float(input('Peso em kilos: '))
        age = int(input('Idade do animal em meses: '))
    except ValueError:
        print('Insira um número válido, para peso 10.5 kg, para idade 10 meses.')
        return
    
    status = 'active'
        
    animal = {
        "id": animal_id,
        "species": species,
        "weight": weight,
        "age": age,
        "status": status
    }

    animals.append(animal)
    save_animals(animals)
    print('Animal cadastrado!')

def update_data():
    animals = load_animals
