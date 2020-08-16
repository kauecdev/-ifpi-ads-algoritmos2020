# Entrada 

number_1 = int(input("Digite o primeiro número inteiro: "))
number_2 = int(input("Digite o segundo número inteiro: "))
number_3 = int(input("Digite o terceiro número inteiro: "))

# Processamento 

r = (number_1 + number_2) ** 2
s = (number_2 + number_3) ** 2
d = (r + s) / 2

# Saída 

print(f"O resultado da expressão D = (R + S) / 2 (onde R = ({number_1} + {number_2})² e S = ({number_2} + {number_3})²) é: {d}.")