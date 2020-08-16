# Entrada

ponto_1_x = float(input("Digite o valor de x em um ponto no plano cartesiano: "))
ponto_1_y = float(input("Digite o valor de y em um ponto no plano cartesiano: "))
ponto_2_x = float(input("Digite o valor de x em um outro ponto no plano cartesiano: "))
ponto_2_y = float(input("Digite o valor de y em um outro ponto no plano cartesiano: "))

# Processamento

d = (((ponto_2_x - ponto_1_x) ** 2) + ((ponto_2_y - ponto_1_y) ** 2)) ** 0.5

# Saída 

print(f"A distância entre os pontos {ponto_1_x,ponto_1_y} e {ponto_2_x,ponto_2_y} é: {d}.")
