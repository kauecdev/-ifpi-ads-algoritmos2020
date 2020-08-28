def main():
    n = int(input("Digite a quantidade de termos a calcular: "))

    # Método com while

    # contador = 0
    # soma = 0

    # while contador < n:
    #     n1 = int(input("Digite o valor do termo: "))
    
    #     soma += n1
    #     media = soma / n
    
    #     contador += 1

    # Método com for

    soma = 0

    for i in range(0, n):
        n1 = int(input("Digite o valor do termo: "))

        soma += n1
        media = soma / n

    print(f'A soma de todos os termos digitados é {soma} e sua média é {media}')



main()


