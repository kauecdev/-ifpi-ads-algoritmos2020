# Entrada

binario = int(input("Digite um número em binário (4 dígitos no máximo) para ser receber o equivalente na base decimal: "))

# Variáveis (Valores de posição)

valor_de_posicao_1 = 2 ** 3
valor_de_posicao_2 = 2 ** 2
valor_de_posicao_3 = 2 ** 1
valor_de_posicao_4 = 2 ** 0

# Processamento 1 (Desmembrar o número)

number_1 = binario // 1000
resto_div_1 = binario % 1000
number_2 = resto_div_1 // 100
resto_div_2 = resto_div_1 % 100
number_3 = resto_div_2 // 10
number_4 = resto_div_2 % 10

# Processamento 2 (Conversão para decimal)

convert_number_1 = number_1 * valor_de_posicao_1
convert_number_2 = number_2 * valor_de_posicao_2 
convert_number_3 = number_3 * valor_de_posicao_3
convert_number_4 = number_4 * valor_de_posicao_4

resultado_final = convert_number_1 + convert_number_2 + convert_number_3 + convert_number_4

# Saída

print(f"O equivalente na base decimal é: {resultado_final}.")
