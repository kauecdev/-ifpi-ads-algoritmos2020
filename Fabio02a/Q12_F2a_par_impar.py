def main():
    numero = int(input("Digite um número: "))

    verificar_impar_par(numero)


def verificar_impar_par(n):
    if (n % 2) == 0:
        print(f"O número {n} é par.")
    else:
        print(f"O número {n} é impar.")


main()
