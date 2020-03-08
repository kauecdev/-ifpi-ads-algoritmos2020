# Hora inicial 

hora_inicial = 6
min_inicial = 52

# Passadas

passada_1 = (8 + (15 / 60))
passada_2 = (7 + (12 / 60)) * 3
passada_3 = passada_1

# Processamento

soma_passadas = passada_1 + passada_2 + passada_3
convert_tempo = (min_inicial + (soma_passadas % 60)) // 60
min_final = int((min_inicial  + (soma_passadas % 60)) % 60)
hora_final = int(hora_inicial + (soma_passadas // 60) + convert_tempo)

# Saída

print(hora_final,min_final)


