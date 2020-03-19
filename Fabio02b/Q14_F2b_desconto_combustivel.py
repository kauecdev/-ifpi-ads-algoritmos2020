def main():
    litros_vedidos = int(input("Digite a quantidade de litros vendido: "))
    tipo_combustivel = str(input("Tipo de combustível desejado (A-álcool, G-gasolina): "))
    
    preco_litro_alcool = 1.90
    preco_litro_gasolina = 2.50

    preco_a_pagar = desconto_combustivel(litros_vedidos,tipo_combustivel,preco_litro_alcool,preco_litro_gasolina)

    print(f"Valor à pagar: R${preco_a_pagar}.")
    

def desconto_combustivel(l,t,pa,pg):
    if t == 'a':
        preco_sem_desconto = l * pa
        if l <= 20:
            return preco_sem_desconto - (((3 / 100) * pa) * l) 
        else:
            return preco_sem_desconto - ((5 / 100) * pa) * l
    elif t == 'g':
        preco_sem_desconto = l * pg
        if l <= 20:
            return preco_sem_desconto - ((4 / 100) * pg) * l
        else:
            return preco_sem_desconto - ((6 / 100) * pg) * l
    else:
        print("Tipo de combustível inválido!")


main()