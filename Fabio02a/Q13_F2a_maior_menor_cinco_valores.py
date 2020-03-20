def main():
    print("Digite cinco números, todos diferentes dos demais.")

    num_1 = int(input("Digite o primeiro número: "))
    num_2 = int(input("Digite o segundo número: "))
    num_3 = int(input("Digite o terceiro número: "))
    num_4 = int(input("Digite o quarto número: "))
    num_5 = int(input("Digite o quinto número: "))

    verificar_maior(num_1,num_2,num_3,num_4,num_5)
    verificar_menor(num_1,num_2,num_3,num_4,num_5)


def verificar_maior(a,b,c,d,e):
    if (a != b and a != c and a != d and a != e) and (b != a and b != c and b != d and b != e) and (c != a and c != b and c != d and c != e) and (d != b and d != c and d != a and d != e) and (e != b and e != c and e != d and e != a):
        if a > b and a > c and a > d and a > e:
            print(f"{a} é o maior.")
        elif b > a and b > c and b > d and b > e:
            print(f"{b} é o maior")
        elif c > a and c > b and c > d and c > e:
            print(f"{c} é o maior")
        elif d > a and d > b and d > c and d > e:
            print(f"{d} é o maior")
        elif e > a and e > b and e > c and e > d:
            print(f"{e} é o maior")
    else: 
        print("Dois ou mais números são iguais.")


def verificar_menor(a,b,c,d,e):
    if (a != b and a != c and a != d and a != e) and (b != a and b != c and b != d and b != e) and (c != a and c != b and c != d and c != e) and (d != b and d != c and d != a and d != e) and (e != b and e != c and e != d and e != a):
        if a < b and a < c and a < d and a < e:
            print(f"{a} é o menor.")
        elif b < a and b < c and b < d and b < e:
            print(f"{b} é o menor.")
        elif c < a and c < b and c < d and c < e:
            print(f"{c} é o menor.")
        elif d < a and d < b and d < c and d < e:
            print(f"{d} é o menor.")
        elif e < a and e < b and e < c and e < d:
            print(f"{e} é o menor.")
    else: 
        print("Dois ou mais números são iguais.")

main()