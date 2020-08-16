# Entrada

metros = int(input("Digite uma medida em m (valor inteiro) para ter o equivalente em km e m: "))

# Processamento

km = metros // 1000
resto_div = metros % 1000

# Saída 

print(f"O valor correspondente em km e metros é {km} quilômetro(s) e {resto_div} metro(s).")
