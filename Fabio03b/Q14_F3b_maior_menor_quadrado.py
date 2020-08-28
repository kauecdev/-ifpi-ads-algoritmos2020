def main():
    n = int(input("Digite um número: "))

    # Método com while

    # quadrado = 2
    # numero_elevado = 1
    # numeros_quadrados = 0

    # while numero_elevado < n:
    #     numeros_quadrados = numero_elevado ** quadrado

    #     if numeros_quadrados >= n:
    #         break
        
    #     numero_elevado += 1

    #     print(numeros_quadrados)

    # print(f"^ É o maior quadrado menor que {n}.")


    # Método com for

    quadrado = 2
    numero_elevado = 1
    numeros_quadrados = 0

    for i in range(numero_elevado, n):
        
        numeros_quadrados = i ** quadrado

        if numeros_quadrados >= n:
            break

        print(numeros_quadrados)

    print(f"^ É o maior quadrado menor que {n}.")

    
main()


