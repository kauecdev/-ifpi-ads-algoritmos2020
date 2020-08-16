# Entrada

fracao_1_numerador = int(input("Digite o numerador da primeira fração: "))
fracao_1_denominador = int(input("Digite o denominador da primeira fração: "))
fracao_2_numerador = int(input("Digite o numerador da segunda fração: "))
fracao_2_denominador = int(input("Digite o denominador da segunda fração: "))

# Processamento 

novo_denominador = fracao_1_denominador * fracao_2_denominador
novo_numerador = ((novo_denominador // fracao_1_denominador) * fracao_1_numerador) + ((novo_denominador //fracao_2_denominador) * fracao_2_numerador)

# Saída

print(f"A soma das frações é: {novo_numerador} / {novo_denominador}.")