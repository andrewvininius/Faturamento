import json

# Leitura dos dados do faturamento diário a partir de um arquivo json
with open('faturamento.json', 'r') as file:
    data = json.load(file)

# Armazenamento dos valores de faturamento diário em um vetor
faturamento_diario = data['faturamento']

# Encontrar o menor e o maior valor de faturamento diário
menor_valor = min(faturamento_diario)
maior_valor = max(faturamento_diario)

# Calcular a média mensal de faturamento, ignorando os dias sem faturamento
dias_com_faturamento = [faturamento for faturamento in faturamento_diario if faturamento > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

# Contar quantos dias tiveram faturamento diário superior à média mensal
dias_acima_da_media = len([faturamento for faturamento in faturamento_diario if faturamento > media_mensal])

# Exibir os resultados
print(f"Menor valor de faturamento diário: R${menor_valor:.2f}")
print(f"Maior valor de faturamento diário: R${maior_valor:.2f}")
print(f"Dias com faturamento diário acima da média: {dias_acima_da_media}")
