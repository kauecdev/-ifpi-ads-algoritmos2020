def main():
    limite_inferior = int(input('Limite inferior: '))
    limite_superior = int(input('Limite superior: '))

    while limite_inferior < limite_superior:
        
        if limite_inferior % 2 != 0 and limite_inferior < limite_superior:
            print(limite_inferior)

        limite_inferior += 1


main()
