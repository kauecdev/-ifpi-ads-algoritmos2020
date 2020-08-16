def main():
    limite = int(input('Número limite: '))
    inicial = 1
    resultado = 0

    while inicial <= limite:
        resultado = resultado + inicial
        inicial += 1

    print(resultado)

main()