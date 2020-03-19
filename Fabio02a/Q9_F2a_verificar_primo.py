def main():
    numero = int(input("Digite um número de 0 a 100: "))

    verificar_primo(numero)

def verificar_primo(n):
    if (n <= 100) and (n >= 0):
        if n == 2 or n == 3:
            print(f"O número {n} é primo.")
        elif n % 1 == 0 and n % 2 != 0 and n % 3 != 0:
            print(f"O número {n} é primo.")
        else: 
            if n != 2:
                print(f"O número {n} não é primo.")
    else: 
        print("Você digitou um número negativo ou maior que 100.")


main()