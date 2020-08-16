def main():
    n = int(input("Digite um valor: "))

    counter = 1

    while counter <= n:
        if (counter % 2 == 0):
            print(counter)
        counter += 1


main()