def main():
    n = int(input("Digite um valor: "))

    # Método com while

    # counter = 1

    # while counter <= n:
    #     if (counter % 2 == 0):
    #         print(counter)
    #     counter += 1

    # Método com for

    for i in range(1,n+1):
        if(i % 2 == 0):
            print(i)


main()