# Entrada

segundos = int(input("Digite um valor de segundos: "))

# Processamento 

eq_horas = segundos // 3600
resto_div_hora = segundos % 3600
eq_minutos = resto_div_hora // 60
resto_div_min = resto_div_hora % 60

# Saída

print(f"O total digitado equivale a {eq_horas} hora(s), {eq_minutos} minuto(s) e {resto_div_min} segundos.")