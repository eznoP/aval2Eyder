
from datetime import datetime
from files import load_data, save_data
from utilitys import clear, return_to_menu

FILENAME = 'movements.json'

def add_movement():                                         # Registra uma movimentação usando a camada de arquivos padrão (data/).
                                                            # Evita criar arquivos na pasta de trabalho atual por acidente.
    movements = load_data(FILENAME)

    data_str = datetime.now().isoformat(sep=' ')
    user_choose = (input(">>> Deseja realmente registrar uma nova movimentação? (Pressione Enter para continuar ou 0 para voltar ao menu): "))
    clear()
    if user_choose == "0":
        clear()
        return
    
    while True:
        description = input(">>> Descrição da movimentação:\n")
        if len(description) < 10:
            input("A movimentação deve ter pelo menos 10 caracteres. Pressione ENTER para tentar novamente.")
            return
        else:
            break
    

    movement = {"date": data_str, "description": description}
    movements.append(movement)

    save_data(FILENAME, movements)
    print("\n\nMovimentação registrada com sucesso!\n\n")
    return_to_menu()    