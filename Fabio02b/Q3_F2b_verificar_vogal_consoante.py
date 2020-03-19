def main():
    letra = str(input("Digite uma letra: "))

    verificar_vogal_consoante(letra)


def verificar_vogal_consoante(l):
    if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
        print("É uma vogal")
    else:
        print("É uma consoante.")


main()