def main():
    numero = int(input("Digite um número para receber o dia correspondente da semana: \n"
                       "1 - Domingo\n"
                       "2 - Segunda-feira\n"
                       "3 - Terça-feira\n"
                       "4 - Quarta-feira\n"
                       "5 - Quinta-feira\n"
                       "6 - Sexta-feira\n"
                       "7 - Sábado\n"
                       "Seu número: "))

    dia_semana(numero)


def dia_semana(n):
    if n == 1:
        print("Domingo")
    elif n == 2:
        print("Segunda-feira")
    elif n == 3:
        print("Terça-feira")
    elif n == 4:
        print("Quarta-feira")
    elif n == 5:
        print("Quinta-feira")
    elif n == 6:
        print("Sexta-feira")
    elif n == 7:
        print("Sábado")
    else: 
        print("Valor Inválido!")


main()