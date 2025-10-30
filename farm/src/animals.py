from utilitys import clear, return_to_menu  
import re
from files import load_data, save_data

FILENAME = 'animals.json'

def add_animal():
    
    animals = load_data(FILENAME) 
    
    try:
        user_choose = (input("Deseja realmente adicionar um novo animal? (Pressione Enter para continuar ou 0 para voltar ao menu): "))
        clear()
        if user_choose == "0":
            clear()
            return

        print('\n==== ADICIONAR NOVO ANIMAL ====\n')
        ID = int(input("> ID do animal (0001): "))
        for a in animals:                                                # VALIDAÇÃO DE ID JÁ EXISTENTE
            if a["id"] == ID:
                clear()
                print("❌ Erro: ID já cadastrado. Utilize um ID diferente.")
                return_to_menu()
                return

        species = input("> Espécie (ex: “bovino”, “caprino”, “ave”, “suíno”): ")         
        if species.lower() not in ["bovino", "caprino", "ave", "suíno"]:   # VALIDAÇÃO DA ESPÉCIE DO ANIMAL
            clear()
            print("❌ Erro: espécie inválida. Utilize apenas 'bovino', 'caprino', 'ave' ou 'suíno'.")
            return_to_menu()
            return
        
        age = int(input("> Idade em meses: "))
        if age < 0:                                                        # VALIDAÇÃO DA IDADE DO ANIMAL
            clear()
            print("❌ Erro: a idade não pode ser negativa.")
            return_to_menu()
            return
        
        weight = float(input("> Peso em Kg: "))
        if weight <= 0:                                                    # VALIDAÇÃO DO PESO DO ANIMAL
            clear()
            print("❌ Erro: o peso deve ser um valor positivo.")
            return_to_menu()
            return
        

        animal = {                                             # PROCESSO DE ADICIONAR ANIMAL
            "id": ID,
            "species": species,
            "age": age,
            "weight": weight,
            "status": "active"
        }


        animals.append(animal)         # ADICIONA O NOVO ANIMAL NA LISTA DE ANIMAIS                                                               
        save_data(FILENAME, animals)   # SALVA O NOVO ANIMAL NA LISTA
        clear()
        print("✅ Animal cadastrado com sucesso!")
        return_to_menu()
    
    except ValueError:
        clear()
        print("❌ Erro: valor inválido.")
        return_to_menu()

def list_animals():                 # FUNÇÃO QUE VERIFICA SE EXISTE ALGUM ANIMAL JÁ CADASTRADO, CASO NÃO HAJA NENHUM ARQUIVO COM A LISTA DE ANIMAIS, 
    animals = load_data(FILENAME)   # SERÁ CRIADO UM NOVO AQUIVO PARA QUE A LISTA DE ANIMAIS SEJA SALVA NELE.
    
    if not animals:
        clear()
        print("Nenhum animal cadastrado.\n\n")
        return_to_menu()
        return
    
    for a in animals:
        print(f"{a['id']} - {a['species']} - {a['age']} anos - {a['weight']} kg - {a['status']}")
        print()
        return_to_menu()
