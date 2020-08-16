# Entrada e variáveis

dias_no_ano = 365
carteira = 20 #(total de cigarros em uma carteira)
anos_fuma = int(input("A quantos anos você fuma? "))
cigarros_dia = int(input("Quantos cigarros você fuma por dia? "))
preco_carteira = float(input("Quanto custa a carteira de cigarros? "))

# Processamento

preco_por_cigarro = preco_carteira / carteira
total_gasto = preco_por_cigarro * cigarros_dia * (anos_fuma * dias_no_ano)

# Saída

print(f"O total gasto é aproximadamente: R${total_gasto}.")