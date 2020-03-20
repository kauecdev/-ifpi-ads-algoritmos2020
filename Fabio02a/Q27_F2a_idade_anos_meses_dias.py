def main():
    inserir_dia_atual = int(input("Dia atual(numérico): "))
    inserir_mes_atual = int(input("Mês atual(numérico): "))
    inserir_ano_atual = int(input("Ano atual(numérico): "))

    inserir_dia_nasc = int(input("Dia do seu nascimento(numérico): "))
    inserir_mes_nasc = int(input("Mês do seu nascimento(numérico): "))
    inserir_ano_nasc = int(input("Ano do seu nascimento(numérico): "))

    dia_atual = validar_dia_atual(inserir_dia_atual)
    mes_atual = validar_mes_atual(inserir_mes_atual)
    dia_nasc = validar_dia_atual(inserir_dia_nasc)
    mes_nasc = validar_mes_nasc(inserir_mes_nasc)

    total_dias_atuais = (inserir_ano_atual * 365) + (mes_atual * 30) + dia_atual
    total_dias_nascimento = (inserir_ano_nasc * 365) + (mes_nasc * 30) + dia_nasc

    diferenca_dias = total_dias_atuais - total_dias_nascimento

    ano_usuario = diferenca_dias // 365
    resto = diferenca_dias % 365
    mes_usario = resto // 30
    dia_usario = resto % 30

    print(f"Você tem {ano_usuario} ano(s), {mes_usario} mes(es) e {dia_usario} dia(s) de vida.")


def validar_dia_atual(da):
    if da > 31:
        print("Você digitou um valor inválido!")
    else:
        return da


def validar_mes_atual(ma):
    if ma > 12:
        print("Você digitou um valor inválido!")
    else:
        return ma


def validar_dia_nasc(dn):
    if dn > 31:
        print("Você digitou um valor inválido!")
    else:
        return dn


def validar_mes_nasc(mn):
    if mn > 31:
        print("Você digitou um valor inválido!")
    else:
        return mn


main()