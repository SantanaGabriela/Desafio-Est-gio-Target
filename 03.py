import pandas as pd

df = pd.read_json('dados.json')

print(df)

faturamento_real = df[df['valor'] > 0]

# menor e maior faturamento
menor_faturamento = faturamento_real['valor'].min()
maior_faturamento = faturamento_real['valor'].max()


media_mensal = faturamento_real['valor'].mean()

# Número de dias com faturamento acima da média mensal
dias_acima_da_media = faturamento_real[faturamento_real['valor'] > media_mensal].shape[0]


print(f"Menor valor de faturamento: R$ {menor_faturamento: }")
print(f"Maior valor de faturamento: R$ {maior_faturamento: }")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")