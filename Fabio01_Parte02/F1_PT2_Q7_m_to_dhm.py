# Entrada

minutos_por_hora = 60
minutos_por_dia = 60 * 24
minutos = int(input("Digite um valor (inteiro) em minutos: "))

# Processamento 

eq_dias = minutos // minutos_por_dia
resto_div_dias = minutos % minutos_por_dia
eq_horas = resto_div_dias // minutos_por_hora
resto_div_min = resto_div_dias % 60


# Saída

print(f"O correspondente em dias, horas e minutos é {eq_dias} dia(s), {eq_horas} hora(s) e {resto_div_min} minuto(s).")
