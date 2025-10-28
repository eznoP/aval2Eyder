import os


def clear():
    os.system("cls")
    os.system("cls" if os.name == "nt" else "clear")

def return_to_menu():
    input("Pressione qualquer ENTER para voltar.  ")
    clear()