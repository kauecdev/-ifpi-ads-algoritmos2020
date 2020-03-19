def main():
    valor_1 = int(input("Digite um valor: "))
    valor_2 = int(input("Digite outro valor: "))
    operadores = int(input("Escolha um operador (1-adição,2-subtração,3-multiplicação,4-divisão): "))

    resultado = executar_operação(valor_1,valor_2,operadores)
    print(f"O resultado da operação escolhida entre os valores {valor_1} e {valor_2} é: {resultado}")

def executar_operação(a,b,c):
    if c == 1:
        soma = a + b
        return soma
    elif c == 2:
        subtrai = a - b
        return subtrai
    elif c == 3:
        multiplica = a * b
        return multiplica
    elif c == 4:
        divide = a / b
        return divide


main()
