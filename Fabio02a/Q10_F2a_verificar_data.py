def main():
    dia = int(input("Dia: "))
    mes = int(input("Mês: "))
    ano = int(input("Ano: "))

    verificar_data(dia,mes,ano)


def verificar_data(d,m,a):
    if (d > 0 and d <= 31) and (m > 0 and m <= 12) and (a > 0):
        print("A data é válida.")
    else: 
        print("A data é inválida.")    

    
main()