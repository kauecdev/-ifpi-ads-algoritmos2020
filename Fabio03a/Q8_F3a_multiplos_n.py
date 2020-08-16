def main():
    numero = int(input('Número: '))
    limite_inferior = int(input('Limite inferior: '))
    limite_superior = int(input('Limite superior: '))

    contador = 1

    while limite_inferior <= limite_superior:
 
        multiplo = numero * contador

        if multiplo > limite_inferior and multiplo < limite_superior:
            print(multiplo)
            limite_inferior += 1
        elif multiplo >= limite_superior:
            break

        contador += 1        
        
        

main()
