def main():
    preco_produto_1 = float(input("Digite o valor do primeiro produto: "))
    preco_produto_2 = float(input("Digite o valor do segundo produto: "))
    preco_produto_3 = float(input("Digite o valor do terceiro produto: "))

    verificar_precos(preco_produto_1,preco_produto_2,preco_produto_3)


def verificar_precos(a,b,c):
    if a < b and a < c and (a != b and a != c):
        print("Recomendo comprar o primeiro produto, pois é o mais barato.")
    elif b < a and b < c and (b != a and b != c):
        print("Recomendo comprar o segundo produto, pois é o mais barato.")
    elif c < a and c < b and (c != a and c != b):
        print("Recomendo comprar o terceiro produto, pois é o mais barato.")
    else:
        print("Dois ou mais produtos tem o mesmo preço.")


main()