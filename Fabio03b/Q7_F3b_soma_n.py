def main():
    limite = int(input('Número limite: '))
    inicial = 1
    resultado = 0

    # Método com while

    # while inicial <= limite:
    #     resultado = resultado + inicial
    #     inicial += 1

    # Método com for

    for i in range(inicial, limite+1):
        resultado += i

    print(resultado)

main()