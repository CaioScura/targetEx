faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total = sum(faturamento.values())

for i in faturamento:
    percentual = faturamento[i]/total * 100

    print(i, "%.2f"%percentual)
