def main():
    numero = int(input("Digite um número para calcular seu fatorial: "))

    # Método com while

    # counter = numero
    # fatorial = 1

    # while counter > 0:
    #     fatorial *= counter
    #     counter -= 1

    # Método com for

    fatorial = 1

    for i in range(1, numero + 1):
        fatorial *= i
        print(fatorial)

    print(f'O fatorial de {numero} é: {fatorial}')


main()
