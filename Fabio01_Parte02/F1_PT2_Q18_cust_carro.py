# Entrada

preco_fabrica = float(input("Digite o valor de fábrica do carro desejado: "))

# Processamento 

porcentagem_distribuidor = preco_fabrica * 0.28
porcentagem_impostos = preco_fabrica * 0.45

preco_final = preco_fabrica + porcentagem_distribuidor + porcentagem_impostos


print(f"O preço final somado com a porcentagem do distribuidor ({porcentagem_distribuidor}) e a porcentagem dos impostos ({porcentagem_impostos}) é igual a {preco_final}.")