def main():
    inicial = int(input('Digite o número para exibir a tabuada desejada: '))
    contador = 1
    limite = 10
    choose_operator(inicial, contador, limite)


def choose_operator(i, c, l):
    print('Escolha o tipo de operação da tabuada: ')
    operador = int(input('1 - adição | 2 - subtração | 3 - multiplicação | 4 - divisão: '))

    if operador == 1:
        while c <= l:
            resultado = c + i
            print(f'{i}+{c}={resultado}')
            c += 1
    elif operador == 2:
        while c <= l:
            resultado = c - i
            print(f'{i}-{c}={resultado}')
            c += 1
    elif operador == 3:
        while c <= l:
            resultado = c * i
            print(f'{i}x{c}={resultado}')
            c += 1
    else:
        while c <= l:
            resultado = c / i
            print(f'{i}/{c}={resultado}')
            c += 1


main()