# Entrada

numbers = int(input("Digite um número de 4 dígitos (no máximo): "))

# Processamento

m = numbers // 1000
resto_div_m = numbers % 1000
c = resto_div_m // 100
resto_div_c = resto_div_m % 100
d = resto_div_c // 10
u = resto_div_c % 10

soma_termos = m + c + d + u

# Saída

print(f"A soma dos elementos do número digitado é: {soma_termos}.")