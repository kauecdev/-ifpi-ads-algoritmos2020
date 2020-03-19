def main():
    num_1 = int(input("Digite um número: "))
    num_2 = int(input("Digite outro número: "))

    verificar_maior(num_1,num_2)


def verificar_maior(a,b):
    if a > b:
        print(f"O número {a} é o maior e o número {b} é o menor.")
    else:
        print(f"O número {b} é o maior e o número {a} é menor.")


main()
