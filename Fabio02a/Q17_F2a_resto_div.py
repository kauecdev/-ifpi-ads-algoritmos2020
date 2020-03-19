def main():
    valor_1 = int(input("Digite um valor: "))
    valor_2 = int(input("Digite outro valor: "))

    resultado = verificar_resto_div(valor_1,valor_2)
    print(resultado)

def verificar_resto_div(a,b):
    resto_div = a % b
    if resto_div == 1:
        return a + b + resto_div
    elif resto_div == 2:
        if (a % 2) == 0 and (b % 2) == 0:
            return ("Ambos são pares.")
        elif (a % 2) == 1 and (b % 2) == 1:
            return ("Ambos são ímpares.")
        elif (a % 2) == 0 and (b % 2) == 1:
            return (f"O número {a} é par e o {b} é impar.")
        elif (a % 2) == 1 and (b % 2) == 0:
            return (f"O número {b} é par e o {a} é impar.")
    elif resto_div == 3:
        return (a + b) * a
    elif resto_div == 4:
        return (a + b) / a
    else: 
        return (a ** 2),(b ** 2)


main()
