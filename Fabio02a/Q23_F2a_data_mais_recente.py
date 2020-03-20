def main():
    print("Digite a primeira data.")
    dia_1 = int(input("Dia data 1(numérico): "))
    mes_1 = int(input("Mês data 1(numérico): "))
    ano_1 = int(input("Ano data 1(numérico): "))

    print("Digite a segunda data.")
    dia_2 = int(input("Dia data 2(numérico): "))
    mes_2 = int(input("Mês data 2(numérico): "))
    ano_2 = int(input("Ano data 2(numérico): "))

    total_dias_data_1 = (ano_1 * 365) + (mes_1 * 30) + dia_1
    total_dias_data_2 = (ano_2 * 365) + (mes_2 * 30) + dia_2

    verificar_mais_recente(total_dias_data_1,total_dias_data_2)


def verificar_mais_recente(data1,data2):
    if data1 > data2:
        print("A primeira data é mais recente que a segunda.")
    else:
        print("A segunda data é mais recente que a primeira.")


main()