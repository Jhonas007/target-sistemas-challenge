import json

with open('faturamento.json') as f:
    faturamentos = json.load(f)

def calcPercent(data):
    soma = 0.0
    porcentagem = []
    for values in data:
        soma += values['faturamento']
    for value in data:
        porcentagem.append({
            "estado": value['estado'],
            "porcentagem": f"{(value['faturamento'] / soma) * 100:.2f}%"
        })
    
    return porcentagem

for porcetagens in calcPercent(faturamentos):
    if(len(porcetagens['estado']) > 2):
        print(f"Já outros estados contribuiam com {porcetagens['porcentagem']}")
    else:
        print(f"O estado {porcetagens['estado']} ajudou com a porcentagem {porcetagens['porcentagem']}")
