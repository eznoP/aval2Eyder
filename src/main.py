from animals import add_animal, list_animals
from plants import add_plant, list_plants
from inputs import add_input, update_stock
from movements import add_movement
from reports import generate_report
import os

def clear():
    os.system("cls")

def menu():
    while True:
        print("\n===== Fazenda Digital =====\n")
        print("1. Cadastrar Animal")
        print("2. Listar Animais\n")
        print("3. Cadastrar Plantação")
        print("4. Listar Plantações\n")
        print("5. Cadastrar Insumo")
        print("6. Atualizar Estoque\n")
        print("7. Registrar Movimentação")
        print("8. Gerar Relatório\n")
        print("0. Sair\n")
        user_choose = input("Escolha uma opção: ")

        if user_choose == "1":
            clear()
            print('\n==== ADICIONAR NOVO ANIMAL ====')
            add_animal()

        elif user_choose == "2":
            clear()
            list_animals()

        elif user_choose == "3":
            clear()
            print('\n==== ADICIONAR NOVA PLANTA ====')
            add_plant()
        
        elif user_choose == "4":
            clear()
            list_plants()
        
        elif user_choose == "5":
            clear()
            print('\n==== ADICIONAR NOVO INSUMO ====')
            add_input()
        
        elif user_choose == "6":
            clear()
            update_stock()
        
        elif user_choose == "7":
            clear()
            add_movement()
        
        elif user_choose == "8":
            clear()
            generate_report()
        
        elif user_choose == "0":
            print("Saindo... até mais 👋")
            break
        else:
            print("❌ Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
