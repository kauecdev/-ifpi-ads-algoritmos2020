# Entrada

nota_1 = float(input("Digite a sua primeira nota: "))
nota_2 = float(input("Digite a sua segunda nota: "))
nota_3 = float(input("Digite a sua terceira nota: "))

peso_1 = float(input("Qual o peso da sua primeira nota: "))
peso_2 = float(input("Qual o peso da sua segunda nota: "))
peso_3 = float(input("Qual o peso da sua terceira nota: "))

# Processamento

nota_peso_1 = nota_1 * peso_1
nota_peso_2 = nota_2 * peso_2
nota_peso_3 = nota_3 * peso_3

soma_notas = nota_peso_1 + nota_peso_2 + nota_peso_3
soma_pesos = peso_1 + peso_2 + peso_3
media_ponderada = soma_notas / soma_pesos

# Saída

print("A sua média ponderada é: ", media_ponderada)