def main():
    valor_hora = float(input("Digite o valor da sua hora: "))
    quantidade_horas = int(input("Digite o sua quantidade de horas: "))

    salario_bruto = valor_hora * quantidade_horas

    taxa_ir = calc_imposto_renda(salario_bruto)

    ir = salario_bruto * (taxa_ir / 100)

    inss = salario_bruto * (10 / 100)

    fgts = salario_bruto * (11 / 100)

    total_descontos = ir + inss

    salario_liquido = salario_bruto - total_descontos

    print(f"Salário Bruto:({valor_hora} * {quantidade_horas})     :R$ {salario_bruto}\n"
    f"(-) IR ({taxa_ir}%)                   :R$ {ir}\n"
    f"(-) INSS (10%)                :R$ {inss}\n"
    f"FGTS (11%)                    :R$ {fgts}\n"
    f"Total de descontos            :R$ {total_descontos}\n"
    f"Salário Líquido               :R$ {salario_liquido}")




def calc_imposto_renda(s):
    if s <= 900:
        return 0
    elif s <= 1500:
        return 5
    elif s <= 2500:
        return 10
    else:
        return 20

main()