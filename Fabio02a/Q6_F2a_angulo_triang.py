def main():
    angulo_1 = int(input("Digite um valor para ser o ângulo de um triângulo: "))
    angulo_2 = int(input("Digite um valor para ser o ângulo de um triângulo: "))
    angulo_3 = int(input("Digite um valor para ser o ângulo de um triângulo: "))

    verificar_triangulo(angulo_1,angulo_2,angulo_3)



def verificar_triangulo(a,b,c):
    if a+b+c == 180 and a < 90 and b < 90 and c < 90:
        print("Forma um triângulo e será acutângulo.")
    elif a+b+c == 180 and a == 90 or b == 90 or c == 90:
        print("Forma um triângulo e será reto.")
    elif a+b+c == 180 and a >= 90 or b >= 90 or c >= 90:
        print("Forma um triângulo e será obtusângulo.")


main()


