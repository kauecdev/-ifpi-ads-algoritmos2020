# Entrada

digitos = int(input("Digite um número com até 3 dígitos: "))

# Processamento 

number_1 = digitos // 100
rest = digitos % 100
number_2 = rest // 10
number_3 = rest % 10

# Saída

print(number_3,number_2,number_1)

