def main():
    a = int(input("Digite o valor A inicial: "))
    limite = int(input("Digite o valor limite: "))
    razao = int(input("Digite o valor da razão: "))

    print(a)

    while a < limite:
        a = a + razao
        if (a > limite):
            break
        print(a)


main()