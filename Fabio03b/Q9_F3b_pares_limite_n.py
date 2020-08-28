def main():
    limite_inferior = int(input('Limite inferior: '))
    limite_superior = int(input('Limite superior: '))

    # Método com while

    # while limite_inferior < limite_superior:
        
    #     if limite_inferior % 2 == 0 and limite_inferior < limite_superior:
    #         print(limite_inferior)

    #     limite_inferior += 1


    # Método com for

    for i in range(limite_inferior, limite_superior):
        if i % 2 == 0 and i < limite_superior:
            print(i)


main()
