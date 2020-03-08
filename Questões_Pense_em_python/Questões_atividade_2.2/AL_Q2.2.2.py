# Declaração de variáveis

quantidade_livros = 60
preco_livro_individual = 24.95
custo_transporte_fixo = 3
custo_transporte_adicional = 0.75

# Processamento

desconto_livraria = preco_livro_individual * 0.6
preco_total_livros = desconto_livraria * quantidade_livros
total_custo = custo_transporte_fixo + (custo_transporte_adicional * 59) + preco_total_livros

# Saída

print(total_custo)