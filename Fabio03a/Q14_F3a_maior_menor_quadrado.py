def main():
    n = int(input("Digite um número: "))

    quadrado = 2
    numero_elevado = 1
    numeros_quadrados = 0

    while numero_elevado < n:
        numeros_quadrados = numero_elevado ** quadrado

        if numeros_quadrados >= n:
            break
        
        numero_elevado += 1

        print(numeros_quadrados)

    print(f"^ É o maior quadrado menor que {n}.")


main()


