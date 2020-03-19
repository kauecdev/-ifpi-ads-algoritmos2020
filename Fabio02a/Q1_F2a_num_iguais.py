def main():
    num_1 = int(input("Digite um número: "))
    num_2 = int(input("Digite um número: "))
    num_3 = int(input("Digite um número: "))

    verificar_iguais(num_1,num_2,num_3)


def verificar_iguais(a,b,c):
    if a == b and a == c and b == c:
        print("Todos os números são iguais.")
    elif a != b and b == c:
        print("Dois números são iguais.")
    elif a == b and a != c:
        print("Dois número são iguais.")
    elif a == c and a != b:
        print("Dois números são iguais.")
    else:
        print("Todos os números são diferentes.")


main()


