def main():
    letra = str(input("Digite seu sexo (letra m ou f): "))

    verificar_sexo(letra)


def verificar_sexo(l):
    if l == 'f':
        print("F - Feminino")
    elif l == 'm':
        print("M - Masculino")
    else:
        print("Sexo inválido.")


main()