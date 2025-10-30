from datetime import datetime, timedelta        # FUNÇÕES QUE ADICIONAM O TIPO DE DATA (YYYY-MM-DD)
from files import load_data, save_data
import re
from utilitys import clear, return_to_menu

FILENAME = 'plants.json'

def add_plant():                       
    
    plants = load_data(FILENAME)
    
    user_choose = (input(">>> Deseja realmente adicionar uma nova planta? (Pressione Enter para continuar ou 0 para voltar ao menu): "))
    clear()
    if user_choose == "0":
        clear()
        return
    
    print('\n==== ADICIONAR NOVA PLANTA ====\n')
    
    ID = input("> ID da plantação (ex: A001): ")
    if not re.fullmatch(r"[A-Za-z]\d{3}", ID):
        print("ID inválido. Use apenas uma letra seguida de três números (ex: A001).")
        return_to_menu()
        return
    
    crop_type = input("> Tipo de cultura (ex: milho, soja, arroz, hortaliça): ")
    try:
        area = float(input("Área (ha): "))
    except ValueError:
        print("❌ Erro: área inválida. Digite um número (ex: 1.5).")
        return

    planting_date = input("> Data de plantio (YYYY-MM-DD): ")

    harvest_time = {"milho": 120, "soja": 130, "arroz": 110}
    harvest_days = harvest_time.get(crop_type.lower(), 100)

    try:
        harvest_date = (datetime.fromisoformat(planting_date) + timedelta(days=harvest_days)).date().isoformat()
    except ValueError:
        print("❌ Data inválida. Use o formato YYYY-MM-DD.")
        return
    


    plant = {
        "id": ID,
        "crop_type": crop_type,
        "area": area,
        "planting_date": planting_date,
        "harvest_date": harvest_date,
        "status": "planted"
    }

    plants.append(plant)
    save_data(FILENAME, plants)
    print("✅ Plantação cadastrada com sucesso!")
    print()
    return_to_menu()

def list_plants():
    plants = load_data(FILENAME)
    if not plants:
        print("Nenhuma plantação cadastrada.\n\n")
        return_to_menu()
        return
    for p in plants:
        print(f"{p['id']} - {p['crop_type']} - {p['area']} ha - colheita em {p['harvest_date']} - {p['status']}\n\n")
        return_to_menu()
