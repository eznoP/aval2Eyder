from datetime import datetime
from files import load_data

def generate_report():
    
    animals = load_data('animals.json')              # CARREGA O ARQUIVO DOS ANIMAIS SALVOS
    plants = load_data('plants.json')                # CARREGA O ARQUIVO DAS PLANTAS SALVAS
    inputs = load_data('inputs.json')                # CARREGA O ARQUIVO DOS INSUMOS SALVOS

    report_lines = [                                 # RELATÓRIO QUE APARECERÁ QUANDO O USUÁRIO SOLICITAR A GERAÇÃO DE RELATÓRIO
        
        f"Relatório - Fazenda",
        f"Data de geração: {datetime.now().strftime('%d/%m/%Y %H:%M')}",
        "-"*50,
        f"Animais cadastrados: {len(animals)}",
        f"Plantações cadastradas: {len(plants)}",
        f"Insumos cadastrados: {len(inputs)}",
        "-"*50,
        "Detalhes de animais:"
    ]

    for a in animals:                   
        report_lines.append(f"{a['id']} - {a['species']} - {a['status']}")

    with open("report.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    print("✅ Relatório gerado em report.txt!")
