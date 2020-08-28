def main():
    a = int(input("Digite o valor A inicial: "))
    limite = int(input("Digite o valor limite: "))
    razao = int(input("Digite o valor da razão: "))

    # Método com while

    # while a < limite:
    #     a = a + razao
    #     if (a > limite):
    #         break
    #     print(a)

    # Método com for

    for i in range(a, limite, razao):
        if(i > limite):
            break
        print(i)


main()