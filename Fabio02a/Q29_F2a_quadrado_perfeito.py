from math import sqrt

def main():
    numero = int(input("Digite um número (de 4 dígitos) para verificar se é um quadrado perfeito: "))

    verificar_quadrado_perfeito(numero)


def verificar_quadrado_perfeito(n):
    num1 = n // 100
    num2 = n % 100
    if sqrt(n) == (num1 + num2):
        print(f"O número {n} é um quadrado perfeito.")
    else:
        print("Não é um quadrado perfeito.")


main()