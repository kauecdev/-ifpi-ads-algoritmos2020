# Entrada

number = int(input("Digite um número inteiro de 3 digitos (no máximo): "))

# Processamento

c = number // 100
resto_div_c = number % 100
d = resto_div_c // 10
u = resto_div_c % 10

inverse = int(str(u) + str(d) + str(c))

diferenca = number - inverse

print(f"A diferença entre o número digitado ({number}) e seu inverso ({inverse}) é: {diferenca}.")