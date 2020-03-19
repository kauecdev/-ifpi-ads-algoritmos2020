def main():
    numero = int(input("Digite um número de 2 dígitos: "))

    d = numero // 10 
    u = numero % 10

    verificar_igualdade(d,u)

def verificar_igualdade(a,b):
    if a == b:
        print("O número das dezenas e o número das unidades são iguais!")
    else:
        print("O número das dezenas e o número das unidades são diferentes!")


main()