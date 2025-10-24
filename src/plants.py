from datetime import datetime, timedelta
from files import load_data, save_data

FILENAME = 'plants.json'

def add_plant():
    try:
        plants = load_data(FILENAME)

        crop_type = input("Tipo de cultura (ex: “milho”, “soja”, “arroz”, “hortaliça”): ")

        area = float(input("Área (ha): "))


        planting_date = input("Data de plantio (YYYY-MM-DD): ")

        harvest_time = {"milho": 120, "soja": 130, "arroz": 110}
        harvest_days = harvest_time.get(crop_type.lower(), 100)
    except ValueError:
        print("❌ Erro: digite palavras para tipo de cultura e números em área.")
    try:
        harvest_date = (datetime.fromisoformat(planting_date) + timedelta(days=harvest_days)).date().isoformat()
    except ValueError:
        print("❌ Data inválida. Use o formato YYYY-MM-DD.")
        return

    plant = {
        "id": input("ID da plantação: "),
        "crop_type": crop_type,
        "area": area,
        "planting_date": planting_date,
        "harvest_date": harvest_date,
        "status": "planted"
    }
    
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
