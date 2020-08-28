def main():
    numero = int(input('Número: '))
    limite_inferior = int(input('Limite inferior: '))
    limite_superior = int(input('Limite superior: '))

    # Método com while

    # contador = 1

    # while limite_inferior <= limite_superior:
 
    #     multiplo = numero * contador

    #     if multiplo > limite_inferior and multiplo < limite_superior:
    #         print(multiplo)
    #         limite_inferior += 1
    #     elif multiplo >= limite_superior:
    #         break

    #     contador += 1        

    # Método com for

    for i in range(1, limite_superior+1):
        multiplo = numero * i

        if multiplo > limite_inferior and multiplo < limite_superior:
            print(multiplo)
        elif multiplo >= limite_superior:
            break
        
        

main()
