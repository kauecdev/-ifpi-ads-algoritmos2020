def main():
    num_1 = int(input('Digite um número: '))
    num_2 = int(input('Digite um número: '))

    verificar_maior_menor(num_1,num_2)

def verificar_maior_menor(a,b):
    if a > b and a != b:
        print(f'O {a} é maior e {b} é menor')
    elif a < b and a != b:
        print(f'O {b} é maior e {a} é menor')
    else:
        print('Eles são iguais')


main()