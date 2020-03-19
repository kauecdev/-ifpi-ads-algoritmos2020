def main():
    opcao = int(input("Digite um número entre 1 e 3: "))
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite um número: "))
    num3 =  int(input("Digite um número: "))

    verificar_iguais(opcao,num1,num2,num3)


def verificar_iguais(a,b,c,d):
    if a == 1:
        print(b)
    elif a == 2:
        print(c)
    elif a == 3:
        print(d)


main()
