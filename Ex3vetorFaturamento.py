import json

# Carrega o JSON
with open('dados.json', 'r') as f:
    dados = json.load(f)
    

menorValor = dados[0]['valor']
maiorValor = 0
total = 0
diasAcimaMedia = 0

for i in dados:
    valor = i['valor']
    total += valor

    if valor < menorValor:
        menorValor = valor
        
    if valor > maiorValor:
        maiorValor = valor

media = total/len(dados)

for i in dados:
    if i['valor'] > media:
        diasAcimaMedia+=1

print("O menor faturamento ocorrido em um dia do mês: %.2f"%menorValor)
print("O maior faturamento ocorrido em um dia do mês: %2f"%maiorValor)
print("Número de dias no mês em que o valor foi superior à média mensal: %2f"%diasAcimaMedia)
