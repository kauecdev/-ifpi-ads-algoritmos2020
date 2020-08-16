# Entrada

digitos = int(input("Digite um número com até 3 dígitos: "))

# Processamento

number_1 = digitos // 100
rest = digitos % 100
number_2 = rest // 10
number_3 = rest % 10

sum_number = number_1 + number_2 + number_3 

# Saída

print("A soma dos três dígitos é: ",sum_number)