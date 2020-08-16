def main():
    n = int(input("Digite a quantidade de termos: "))

    contador = 0
    maior = 0

    while contador < n:
        n1 = int(input("Digite o valor do termo: "))

        if (n1 > maior):
            maior = n1
    
        contador += 1

    print(maior)

    
main()


