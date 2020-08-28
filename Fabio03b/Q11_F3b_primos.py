def main():
    limite_inferior = int(input('Limite inferior: '))
    limite_superior = int(input('Limite superior: '))

    # Método com while

    # while limite_inferior < limite_superior:
        
    #     if limite_inferior < 10 and limite_inferior == 2 or limite_inferior == 3 or limite_inferior == 5 or limite_inferior == 7:
    #         print(limite_inferior)
    #     elif limite_inferior > 10 and limite_inferior < 20 and limite_inferior % 2 != 0 and limite_inferior % 3 != 0 and limite_inferior % 5 != 0 and limite_inferior % 7 != 0 or limite_inferior == 11 or limite_inferior == 13 or limite_inferior == 17:
    #         print(limite_inferior)
    #     elif limite_inferior > 20 and limite_inferior % 2 != 0 and limite_inferior % 3 != 0 and limite_inferior % 5 != 0 and limite_inferior % 7 != 0 and limite_inferior % 11 != 0 and limite_inferior % 13 != 0 and limite_inferior % 17 != 0:
    #         print(limite_inferior)
            

    #     limite_inferior += 1

    # Método com for

    for i in range(limite_inferior, limite_superior):
        if i < 10 and i == 2 or i == 3 or i == 5 or i == 7:
            print(i)
        elif i > 10 and i < 20 and i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 or i == 1 or i == 13 or i == 17:
            print(i)
        elif i > 20 and i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 or i == 1 or i == 13 or i == 17:
            print(i)

main()
