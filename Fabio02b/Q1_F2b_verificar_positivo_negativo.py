def main():
    numero = float(input("Digite um número positivo ou negativo: "))

    verificar_positivo_negativo(numero)


def verificar_positivo_negativo(n):
    if n >= 0:
        print("O número é positivo.")
    else: 
        print("O número é negativo.")


main()