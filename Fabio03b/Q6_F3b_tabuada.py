def main():
    inicial = int(input('Digite o número para exibir a tabuada desejada: '))
    contador = 1
    limite = 10
    choose_operator(inicial, contador, limite)


def choose_operator(ini, c, l):
    print('Escolha o tipo de operação da tabuada: ')
    operador = int(input('1 - adição | 2 - subtração | 3 - multiplicação | 4 - divisão: '))

    if operador == 1:
        for i in range(1,l+1):
            resultado = i + ini
            print(f'{ini}+{c}={resultado}')
            c += 1
    elif operador == 2:
        for i in range(1,l+1):
            resultado = i - ini
            print(f'{ini}-{c}={resultado}')
            c += 1
    elif operador == 3:
        for i in range(1,l+1):
            resultado = i * ini
            print(f'{ini}x{c}={resultado}')
            c += 1
    else:
        for i in range(1,l+1):
            resultado = i / ini
            print(f'{ini}/{c}={resultado:.2f}')
            c += 1


main()