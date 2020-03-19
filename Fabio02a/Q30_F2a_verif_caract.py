def main(): 
    numero = int(input("Digite um número de 4 dígitos: "))

    resultado = calculo(numero)
    verificacao = verificar_se_iguais(numero,resultado)
    
    
def calculo(n):
    num_1 = n // 100
    num_2 = n % 100
    soma = num_1 + num_2
    numero_digitado = soma ** 2
    return numero_digitado


def verificar_se_iguais(a,b):
    if a == b:
        print("Este número obedece à caraterística, pois ele é igual ao resultado do cálculo.")
    else:
        print("Este número não obedece à caraterística, pois ele não é igual ao resultado do cálculo.")

main()


