# Entrada

total_dias_ano = 365
total_dias_mes = 30

anos = int(input("Quantos anos você tem? "))
meses = int(input("E quantos meses? "))
dias = int(input("E quantos dias? "))

# Processamento

dias_em_ano = anos * total_dias_ano
dias_em_meses = meses * total_dias_mes

total_dias = dias_em_ano + dias_em_meses + dias


print(f"A quantidade aproximada de dias que você já viveu é: {total_dias}.")