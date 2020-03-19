from math import sqrt as raiz_quadrada

def main():
    a = int(input("Digite o coeficiente A: "))
    b = int(input("Digite o coeficiente B: "))
    c = int(input("Digite o coeficiente C: "))

    raizes = calcular_equ_2_grau(a,b,c)
    print(f'As raízes resultantes dos coeficientes {a},{b} e {c}, são: {raizes}.')


def calcular_equ_2_grau(a,b,c):
    if a != 0:
        formula_delta = (b ** 2) - 4 * a * c
        x1 = (-b + (raiz_quadrada(formula_delta))) / (2 * a)
        x2 = (-b - (raiz_quadrada(formula_delta))) / (2 * a)
        return x1,x2
    else: 
        print("O coeficiente A não pode ser zero.")


main()