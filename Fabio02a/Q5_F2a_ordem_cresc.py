def main():
    num_1 = int(input("Digite um número: "))
    num_2 = int(input("Digite um número: "))
    num_3 = int(input("Digite um número: "))

    verificar_maior(num_1,num_2,num_3)

def verificar_maior(a,b,c):
    if a > b and a > c and b > c and (a != b and a != c and b != c):
        print(a,b,c)
    elif a > b and a > c and c > b and (a != b and a != c and b != c):
        print(a,c,b)
    elif b > a and b > c and a > c and (b != a and b != c and a != c):
        print(b,a,c)
    elif b > a and b > c and c > a and (b != a and b != c and a != c):
        print(b,c,a)
    elif c > a and c > b and a > b and (c != a and c != a and b != a):
        print(c,a,b)
    elif c > a and c > b and b > a and (c != a and c != a and b != a):
        print(c,b,a)
    else: 
        print("Dois ou mais números são iguais!")


main()