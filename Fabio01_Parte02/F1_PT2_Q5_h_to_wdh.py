# Entrada

horas_por_dia = 24
horas = int(input("Digite um valor(inteiro) de horas: "))

# Processamento

horas_por_semana = horas_por_dia * 7
horas_semana = horas // horas_por_semana
resto_div_sem = horas % horas_por_semana
horas_dia =  resto_div_sem // horas_por_dia
resto_div_dia = resto_div_sem % horas_por_dia

print(f"O total correspondente em semanas, dias e horas é {horas_semana} semana(s), {horas_dia} dia(s) e {resto_div_dia} hora(s).")