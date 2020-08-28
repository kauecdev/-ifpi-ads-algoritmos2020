def main():
    n = int(input("Digite um número: "))

    # Método com while

    # numero_soma = n + 1

    # contador = 0

    # while contador < 5:
    #     print(n)
    
    #     n += numero_soma
    #     numero_soma += 1
    #     contador += 1

    # Método com for

    numero_soma = n + 1

    for i in range(0, 5):
        print(n)

        n += numero_soma
        numero_soma += 1


main()


