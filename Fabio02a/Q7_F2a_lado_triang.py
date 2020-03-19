def main():
    lado_1 = int(input("Digite um valor para ser o lado de um triângulo: "))
    lado_2 = int(input("Digite um valor para ser o lado de um triângulo: "))
    lado_3 = int(input("Digite um valor para ser o lado de um triângulo: "))

    verificar_triangulo(lado_1,lado_2,lado_3)

def verificar_triangulo(a,b,c):
    if (a + b > c) and (a + c > b) and (c + b > a) and (a == b == c) and (a,b,c != 0):
        print("Forma um triângulo e será equilátero.")
    elif (a + b > c) and (a + c > b) and (c + b > a) and a == b or a == c or b == c and (a,b,c != 0):
        print("Forma um triângulo e será isósceles.")
    elif (a + b > c) and (a + c > b) and (c + b > a) and a != b and a != c and c != b and (a,b,c != 0):
        print("Forma um triângulo e será escaleno.")
    else: 
        print("Não forma um triângulo.")


main()

