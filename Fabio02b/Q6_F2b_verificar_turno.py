def main():
    turno = str(input("Digite seu turno (m-matutino, v-vespertino ou n-noturno): "))

    verificar_turno(turno)


def verificar_turno(t):
    if t == 'm':
        print("Bom Dia!")
    elif t == 'v':
        print("Boa Tarde!")
    elif t == 'n':
        print("Boa Noite!")
    else:
        print("Valor Inválido!")


main()