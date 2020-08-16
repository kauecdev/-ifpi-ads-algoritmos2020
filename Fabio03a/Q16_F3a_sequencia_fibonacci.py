def main():
    n = int(input("Digite um número que seja maior ou igual a 2: "))

    sequencia_fibonnaci = n
    iterador = n - 1

    contador = 0

    if n <= 1:
        print("O número deve ser 2 ou maior.")
    else: 
        while contador < n:
            print(sequencia_fibonnaci)
            sequencia_fibonnaci = sequencia_fibonnaci + iterador
            iterador += 1
            contador += 1


main()


