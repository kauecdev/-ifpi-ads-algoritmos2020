# Entrada e Variáveis

nota_1 = 50
nota_2 = 10
nota_3 = 5 
nota_4 = 1
valor = int(input("Quanto você deseja sacar? "))

# Processamento

valor_recebido_1 = valor // nota_1
resto_div_1 = valor % nota_1
valor_recebido_2 = resto_div_1 // nota_2
resto_div_2 = resto_div_1 % nota_2
valor_recebido_3 = resto_div_2 // nota_3
valor_recebido_4 = resto_div_2 % nota_3

# Saída

print(f"Você receberá: {valor_recebido_1} nota(s) de R$50, {valor_recebido_2} nota(s) de R$10, {valor_recebido_3} nota(s) de R$5 e {valor_recebido_4} nota(s) de R$1.")