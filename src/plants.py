from datetime import datetime, timedelta        # FUNÇÕES QUE ADICIONAM O TIPO DE DATA (YYYY-MM-DD)
from files import load_data, save_data

FILENAME = 'plants.json'

def add_plant():                       
    print('\n==== ADICIONAR NOVA PLANTA ====')
    # Coleta entradas do usuário com validação
    crop_type = input("Tipo de cultura (ex: milho, soja, arroz, hortaliça): ")
    try:
        area = float(input("Área (ha): "))
    except ValueError:
        print("❌ Erro: área inválida. Digite um número (ex: 1.5).")
        return

    planting_date = input("Data de plantio (YYYY-MM-DD): ")

    harvest_time = {"milho": 120, "soja": 130, "arroz": 110}
    harvest_days = harvest_time.get(crop_type.lower(), 100)

    try:
        harvest_date = (datetime.fromisoformat(planting_date) + timedelta(days=harvest_days)).date().isoformat()
    except ValueError:
        print("❌ Data inválida. Use o formato YYYY-MM-DD.")
        return

    # Monta o dicionário da plantação
    plant = {
        "id": input("ID da plantação: "),
        "crop_type": crop_type,
        "area": area,
        "planting_date": planting_date,
        "harvest_date": harvest_date,
        "status": "planted"
    }

    plants = load_data(FILENAME)
    plants.append(plant)
    save_data(FILENAME, plants)
    print("✅ Plantação cadastrada com sucesso!")

def list_plants():
    plants = load_data(FILENAME)
    if not plants:
        print("Nenhuma plantação cadastrada.")
        return
    for p in plants:
        print(f"{p['id']} - {p['crop_type']} - {p['area']} ha - colheita em {p['harvest_date']} - {p['status']}")
