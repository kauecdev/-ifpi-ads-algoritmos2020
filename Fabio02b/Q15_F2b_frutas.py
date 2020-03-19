def main():
    quantidade_morangos_comprado = float(input("Digite o valor (em kg) de morangos comprados: "))
    quantidade_macas_comprada = float(input("Digite o valor (em kg) de maçãs comprados: "))

    total_quilos_comprado = quantidade_morangos_comprado + quantidade_macas_comprada

    preco_morango = valor_kg_morango(quantidade_morangos_comprado)
    preco_maca = valor_kg_maca(quantidade_macas_comprada)

    valor_total_a_pagar = (preco_morango * quantidade_morangos_comprado) + (preco_maca * quantidade_macas_comprada)

    desconto = verificar_desconto(total_quilos_comprado,valor_total_a_pagar)

    valor_final = valor_total_a_pagar - ((desconto / 100) * valor_total_a_pagar)
    
    print(f"O cliente pagará um total de: R$ {valor_final}.")

def valor_kg_morango(qmo):
    if qmo <= 5:
        preco_por_kg = 2.50
        return preco_por_kg
    else:
        preco_por_kg = 2.20
        return preco_por_kg


def valor_kg_maca(qma):
    if qma <= 5:
        preco_por_kg = 1.80
        return preco_por_kg
    else: 
        preco_por_kg = 1.50
        return preco_por_kg


def verificar_desconto(t,v):
    if t > 8 or v > 25.00:
        return 10
    else:
        return 0

main()