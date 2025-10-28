from animals import add_animal, list_animals
from plants import add_plant, list_plants
from inputs import add_input, update_stock
from movements import add_movement
from reports import generate_report
import os
from utilitys import clear

def menu():
    while True:
        print("\n===== Fazenda Digital =====\n")                     # MENU INTERATIVO COM USUÁRIO
        print("1. Cadastrar Animal")                                 # CASO USUÁRIO DIGITAR 1,2,3,4,5,6,7,8, ABRIRÁ FUNÇÕES QUE
        print("2. Listar Animais\n")                                 # INTERAGEM COM A FAZENDA, CASO DIGITAR 0(ZERO) O SISTEMA FECHA
        print("3. Cadastrar Plantação")
        print("4. Listar Plantações\n")
        print("5. Cadastrar Insumo")
        print("6. Atualizar Estoque\n")
        print("7. Registrar Movimentação")
        print("8. Gerar Relatório\n")
        print("0. Sair\n\n")

        user_choose = input("Escolha uma opção:  ")

        if user_choose == "1":
            clear()
            add_animal()

        elif user_choose == "2":
            clear()
            list_animals()
            clear()

        elif user_choose == "3":
            clear()
            add_plant()
        
        elif user_choose == "4":
            clear()
            list_plants()
            clear()
        
        elif user_choose == "5":
            clear()
            add_input()
        
        elif user_choose == "6":
            clear()
            update_stock()
            clear()
        
        elif user_choose == "7":
            clear()
            add_movement()
            clear()

        elif user_choose == "8":
            clear()
            generate_report()

        elif user_choose == "0":
            print("Saindo... até mais 👋")
            break
        else:
            clear()

if __name__ == "__main__":  
    menu()
