# Entrada

meses_por_ano = 12
meses = int(input("Digite um número (inteiro) de meses: "))

# Processamento

meses_ano = meses // meses_por_ano
meses_mes = meses % meses_por_ano

# Saída

print(f"O correspondente em anos e meses é {meses_ano} ano(s) e {meses_mes} mes(es).")