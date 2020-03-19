def main():
    tipo_carne = str(input("Qual tipo de carne deseja? (f-Filé,a-Alcatra ou p-Picanha): "))
    quantidade_kg = float(input("E quantos Kg deseja?: "))

    preco_kg_por_tipo = verificar_preco_tipo(tipo_carne,quantidade_kg)

    preco_da_compra = quantidade_kg * preco_kg_por_tipo

    forma_pagamento = str(input(f"O preço total da compra é: R$ {preco_da_compra}\n"
          f"Como deseja realizar o pagamento? Em dinheiro ou com os Cartões Tabajara?\n"
          "(lembrando que pagando com Cartão Tabajara, o senhor(a) receberá 10% de desconto\n"
          "Forma de pagamento(d-Dinheiro ou c-Cartão Tabajara): "))

    desconto = verificar_forma_pagamento(forma_pagamento,preco_da_compra)

    valor_final = preco_da_compra - desconto

    print("        *CUPOM FISCAL*        \n\n"
          "Tipo de carne\n"
         f"(f-Filé,a-Alcatra ou p-Picanha):             {tipo_carne}\n"
         f"Quantidade:                                  {quantidade_kg} Kg\n"
         f"Preço total:                               R${preco_da_compra}\n"
          "Forma de pagamento\n"
         f"(d-Dinheiro ou c-Cartão Tabajara):           {forma_pagamento}\n"
         f"Valor do desconto:                         R${desconto}\n"
         f"Valor a pagar:                             R${valor_final}")

def verificar_preco_tipo(tc,qkg):
    if tc == 'f':
        if qkg >= 5:
            preco_por_kg = 4.90
            return preco_por_kg
        else: 
            preco_por_kg = 5.80
            return preco_por_kg
    elif tc == 'a':
        if qkg >= 5:
            preco_por_kg = 5.90
            return preco_por_kg
        else: 
            preco_por_kg = 6.80
            return preco_por_kg
    elif tc == 'p':
        if qkg >= 5:
            preco_por_kg = 6.90
            return preco_por_kg
        else: 
            preco_por_kg = 7.80
            return preco_por_kg
    else: 
        print("Você digitou um valor inválido!")


def verificar_forma_pagamento(f,p):
    if f == 'd':
        return 0
    elif f == 'c':
        return (10 / 100) * p
    else:
        print("Valor digitado inválido!")

main()