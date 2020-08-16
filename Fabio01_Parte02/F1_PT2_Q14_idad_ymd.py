# Entrada

total_dias_anos = 365
total_meses_anos = 12
total_dias_meses = 30
idade_dias = int(input("Digite sua idade em dias: "))

# Processamento 

anos_dias = idade_dias // total_dias_anos
resto_div_anos = idade_dias % total_dias_anos
meses_dias = resto_div_anos // total_dias_meses
dias = resto_div_anos % total_dias_meses

# Saída

print(f"A sua idade expressa em anos, meses e dias (aproximadamente) é: {anos_dias} anos, {meses_dias} meses e {dias} dias.")