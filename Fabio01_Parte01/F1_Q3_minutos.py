# Entrada 

time_minute = int(input("Digite o valor em minutos: "))

# Processamento 

convert_1 = time_minute // 60
convert_2 = time_minute % 60

# Saída 

print("O total de horas e minutos é: ",convert_1,"hora(s) e",convert_2,"minuto(s).")
