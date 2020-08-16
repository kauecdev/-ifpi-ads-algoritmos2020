# Entrada

valor = int(input("Digite o valor da mercadoria: "))

# Processamento 

div = valor // 3
resto = valor % 3
entrada = div + resto
parcelas = (valor - entrada) / 2

# Saída

print(f"O valor da entrada será R${entrada} e o valor de cada parcela será R${parcelas}.")