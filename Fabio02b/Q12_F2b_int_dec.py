def main():
    numero = float(input("Digite um número (inteiro ou decimal): "))

    verificar_int_dec(numero)


def verificar_int_dec(n):
    if n // 1 == n:
        print(f"{n} é um número inteiro.")
    else:
        print(f"{n} é um número decimal.")


main()