import json

with open('dados.json') as f:
    dados = json.load(f)


def menorFaturamento(data):
    numbers = []
    men_faturamento = 0

    for values in data:
        numbers.append(values['valor'])

    men_faturamento = min(numbers)
    
    return men_faturamento
    
def diasComZero(data):
    daysWithZero = []
    quantItems = 0
    dias = ""

    for values in data:
        if(values['valor'] == 0.0):
            daysWithZero.append(values['dia'])
            quantItems += 1
    iteracao = 0
    while iteracao < quantItems:
        if(iteracao == quantItems - 1):
            dias += f"{daysWithZero[iteracao]}"
        else:
            dias += f"{daysWithZero[iteracao]}, "
        iteracao += 1
    if(quantItems > 1):
        return f"Foi registrado faturamento em R$0.0 nos dias: {dias}"
    else:
        return f"Menor faturamento: R${menorFaturamento(data)}"
    
def maiorFaturamento(data):
    numbers = []
    max_faturamento = 0

    for values in data:
        numbers.append(values['valor'])
    
    max_faturamento = max(numbers)
    return max_faturamento

def mediaFaturamento(data):
    numbers = []
    med_faturamento = 0
    sequencia = 0

    for values in data:
        if(values['valor'] == 0.0):
            continue

        numbers.append(values['valor'])

    med_faturamento = sum(numbers) / len(numbers)

    for number in numbers:
        if(number > med_faturamento):
            sequencia += 1

    return sequencia

print(f"Maior faturamento: R${maiorFaturamento(dados)}")
print(diasComZero(dados))
print(f"Dias melhores que a média mensal: {mediaFaturamento(dados)} dias")