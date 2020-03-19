def main():
    altura = float(input("Digite sua altura(em metros): "))
    peso = float(input("Digite seu peso(em kg): "))

    imc = peso / (altura**2)

    verficar_imc(imc)


def verficar_imc(i):
    if i < 25:
        print("Seu peso está normal.")
    elif i < 25 and i <= 30:
        print("Você está obeso.")
    else:
        print("Você tem obesidade mórbida.")
    

main()
