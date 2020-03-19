def main():
    num_1 = int(input("Digite um número: "))
    num_2 = int(input("Digite um número: "))
    num_3 = int(input("Digite um número: "))

    verificar_maior(num_1,num_2,num_3)


def verificar_maior(a,b,c,):
    if a > b and a > c and (a != b and a != c):
        print(f"O número {a} é o maior.")
    elif b > a and b > c and (b != a and b != c):
        print(f"O número {b} é o maior.")
    elif c > a and c > b and (c != a and c != a):
        print(f"O número {c} é o maior.")
    else: 
        print("Dois ou mais números são iguais.")


main()