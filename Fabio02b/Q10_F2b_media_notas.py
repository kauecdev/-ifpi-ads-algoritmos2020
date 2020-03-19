def main():
    nota_1 = float(input("Digite sua primeira nota: "))
    nota_2 = float(input("Digite sua segunda nota: "))

    media = (nota_1 + nota_2) / 2

    resultado = verificar_media(media)
    
    print(f"Notas:               {nota_1} e {nota_2}\n"
          f"Média:               {media}\n"
          f"Aproveitamento:      {resultado}")


def verificar_media(m):
    if m >= 9:
        return "A\n\n""APROVADO"
    elif m >= 7.5:
        return "B\n\n""APROVADO"
    elif m >= 6:
        return "C\n\n""APROVADO"
    elif m >= 4:
        return "D\n\n""REPROVADO"
    else:
        return "E\n\n""REPROVADO"


main()
