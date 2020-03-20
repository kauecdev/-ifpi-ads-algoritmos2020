def main():
    dia_atual = int(input("Dia atual(numérico): "))
    mes_atual = int(input("Mês atual(numérico): "))
    ano_atual = int(input("Ano atual(numérico): "))

    dia_nasc = int(input("Dia do seu nascimento(numérico): "))
    mes_nasc = int(input("Mês do seu nascimento(numérico): "))
    ano_nasc = int(input("Ano do seu nascimento(numérico): "))

    
    calc_anos(dia_atual,dia_nasc,mes_atual,mes_nasc,ano_atual,ano_nasc)



def calc_anos(dia_atual,dia_nasc,mes_atual,mes_nasc,ano_atual,ano_nasc):
    anos = ano_atual - ano_nasc
    if ((mes_atual or mes_nasc) > 12) or ((dia_atual or dia_nasc) > 31) or (ano_atual < ano_nasc):
        print("Você digitou um valor inválido.")
    elif mes_atual < mes_nasc:
        anos -= 1
        print(f"Você tem {anos} anos")
    else:
        print(f"Você tem {anos} anos.")

main()