import json
from datetime import datetime

# Lê o arquivo JSON com os dados de faturamento diário
with open('faturamento.json') as f:
    data = json.load(f)

# Inicializa as variáveis para o menor e maior valor de faturamento
menor_valor = float('inf')
maior_valor = float('-inf')

# Calcula o menor e o maior valor de faturamento diário
for dia, valor in data.items():
    if valor:
        valor = float(valor)
        if valor < menor_valor:
            menor_valor = valor
        if valor > maior_valor:
            maior_valor = valor

# Calcula a média mensal de faturamento, excluindo os dias sem faturamento
valores = [float(v) for v in data.values() if v]
media = sum(valores) / len(valores)

# Conta o número de dias em que o valor de faturamento diário foi superior à média mensal
dias_acima_da_media = sum(1 for v in valores if v > media)

# Imprime os resultados
print(f'Menor valor de faturamento diário: R${menor_valor:.2f}')
print(f'Maior valor de faturamento diário: R${maior_valor:.2f}')
print(f'Número de dias acima da média mensal de faturamento: {dias_acima_da_media}')
