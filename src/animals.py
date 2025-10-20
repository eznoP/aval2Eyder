
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

    animal_id = int(input('Adicione o ID do animal: ').strip)  # CADSATRO DO ID DO ANIMAL
    if any(a['id'] == animal_id for a in animals):             # EVITAR QUE SEJAM CADASTRADOS IDs IGUAIS
        print('ID já cadastrado.') 
        return
    
    species = input('Insira a espécie do animal (bovino, caprino, aves, etc): ').strip  # CADASTRAR A ESPÉCIE DO ANIMAL
    
    try:
        weight = float(input('Peso em kilos: '))                                       # CADASTRAR PESO E IDADE DO ANIMAL
        age = int(input('Idade do animal em meses: '))
    except ValueError:
        print('Insira um número válido, para peso 10.5 kg, para idade 10 meses.')     # CASO O USUÁRIO NÃO COLOQUE UM NÚMERO VÁLIDO
        return
    
    status = 'active'   # POR PADRÃO O STATUS DO ANIMAL JÁ VEM ATIVO
        
    animal = {                        # DICIONÁRIO PARA ARMAZENAR AS INFORMAÇÕES DO ANIMAL
        "id": animal_id,
        "species": species,
        "weight": weight,
        "age": age,
        "status": status
    }

    animals.append(animal)           # ADICIONAR O NOVO ANIMAL NA LISTA
    save_animals(animals)            # SALVAR O ANIMAL
    print('Animal cadastrado!')      # FEEDBACK PARA O USUÁRIO

def update_data():
    animals = load_animals
