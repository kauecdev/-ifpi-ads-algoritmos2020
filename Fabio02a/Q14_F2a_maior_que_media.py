def main():
    num_1 = int(input("Digite um número: "))
    num_2 = int(input("Digite um número: "))
    num_3 = int(input("Digite um número: "))
    num_4 = int(input("Digite um número: "))
    num_5 = int(input("Digite um número: "))

    resultado_media = calcular_media(num_1,num_2,num_3,num_4,num_5)
    verificar_maior_que_media(num_1,num_2,num_3,num_4,num_5,resultado_media)


def calcular_media(a,b,c,d,e):
    media = (a + b + c + d + e) / 5
    return media


def verificar_maior_que_media(a,b,c,d,e,media):
    if a > media:
        print(f"O número {a} é maior que a média.")
    if b > media:
        print(f"O número {b} é maior que a média.")
    if c > media:
        print(f"O número {c} é maior que a média.")
    if d > media:
        print(f"O número {d} é maior que a média.")
    if e > media:
        print(f"O número {e} é maior que a média.")
    else: 
        print("Nenhum dos números é maior que a média.")
    
main()