# Entrada 

time_hour = int(input("Digite as horas: "))
time_minute = int(input("Digite os minutos: "))

# Processamento

convert_hour = time_hour * 60
total_minutes = convert_hour + time_minute


# Saída

print("O total de minutos é: ", total_minutes)
