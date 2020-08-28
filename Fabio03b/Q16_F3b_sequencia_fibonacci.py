def main():
    n = int(input("Digite um número que seja maior ou igual a 2: "))

    # Método com while

    # sequencia_fibonnaci = n
    # iterador = n - 1

    # contador = 0

    # if n <= 1:
    #     print("O número deve ser 2 ou maior.")
    # else: 
    #     while contador < n:
    #         print(sequencia_fibonnaci)
    #         sequencia_fibonnaci = sequencia_fibonnaci + iterador
    #         iterador += 1
    #         contador += 1

    # Método com for

    sequencia_fibonnaci = n
    iterador = n - 1

    if n <= 1:
        print("O número deve ser 2 ou maior.")
    else:
        for i in range(0, n):
            print(sequencia_fibonnaci)
            sequencia_fibonnaci += iterador
            iterador += 1


main()


