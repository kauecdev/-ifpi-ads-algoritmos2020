def main():
    lado_1 = float(input("Digite o tamanho do primeiro lado de um triângulo: "))
    lado_2 = float(input("Digite o tamanho do segundo lado de um triângulo: "))
    lado_3 = float(input("Digite o tamanho do terceiro lado de um triângulo: "))

    hipotenusa_catetos(lado_1,lado_2,lado_3)


def hipotenusa_catetos(a,b,c):
    if a > b and a > c:
        print(f"{a} é a hipotenusa e {b} e {c} são os catetos.")
    elif b > a and b > c:
        print(f"{b} é a hipotenusa e {a} e {c} são os catetos.")
    elif c > a and c > b:
        print(f"{c} é a hipotenusa e {a} e {b} são os catetos.")


main()