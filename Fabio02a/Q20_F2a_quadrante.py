def main():
    angulo = float(input("Digite o valor de um ângulo (entre 0° e 360°): "))

    verificar_quadrante(angulo)


def verificar_quadrante(a):
    if a > 0 and a <= 90:
        print(f"O ângulo {a} está no primeiro quadrante.")
    elif a < 90 and a <= 180:
        print(f"O ângulo {a} está no segundo quadrante.")
    elif a > 180 and a <= 270:
        print(f"O ângulo {a} está no terceiro quadrante.")
    elif a > 270 and a <= 360:
        print(f"O ângulo {a} está no quarto quadrante.")
    else: 
        "Você digitou um valor negativo ou maior que 360°"


main()