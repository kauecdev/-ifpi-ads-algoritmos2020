def main():
    numero = int(input("Digite um número para calcular seu fatorial: "))

    counter = numero
    fatorial = 1

    while counter > 0:
        fatorial *= counter
        counter -= 1

    print(f'O fatorial de {numero} é: {fatorial}')


main()
