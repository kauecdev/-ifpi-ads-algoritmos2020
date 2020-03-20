def main():
    num = float(input("Digite um número fracionário para ser arredondado: "))

    arredondar(num)


def arredondar(n):
    if n % 1 >= 0.5:
        n = (n // 1) + 1
        print(n)
    else: 
        n = n - (n % 1)
        print(n)


main()