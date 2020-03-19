def main():
    salario = float(input("Digite seu salário atual: R$ "))
    
    taxa = calcular_reajuste(salario)
    aumento = (taxa / 100) * salario
    salario_reajustado = salario + aumento

    print(f"O seu salário era R${salario},\na taxa de reajuste aplicada foi de {taxa}%,\no valor do seu aumento será R${aumento},\no seu novo salário será R${salario_reajustado}")


def calcular_reajuste(s):
    if s <= 280:
        return 20
    elif s < 700:
        return 15
    elif s < 1500:
        return 10
    else:
        return 5

main()