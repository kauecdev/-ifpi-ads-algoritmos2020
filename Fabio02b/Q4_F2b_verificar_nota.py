def main():
    nota_1 = float(input("Digite a primeira nota: "))
    nota_2 = float(input("Digite a segunda nota: "))

    verificar_media(nota_1,nota_2)


def verificar_media(a,b):
    media = (a + b) / 2
    if media == 10:
        print("Aprovado com distinção!")
    elif media >= 7 and media < 10:
        print("Aprovado!")
    else: 
        print("Reprovado!")


main()
    