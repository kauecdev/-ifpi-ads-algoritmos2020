def main():
    print("Cálculo do Imposto de Renda com a tabela sem correção e com tabela corrigida.")

    renda = float(input("Insira sua renda mensal: R$ "))

    ir_antigo = calcular_ir_sem_reajuste(renda)
    ir_reajustado = calcular_ir_com_reajuste(renda)

    print(f"De acordo com a tabela sem reajuste, quem recebe R$ {renda}, deverá pagar R$ {ir_antigo:.2f} de imposto de renda.\n"
    f"Já de acordo com a tabela reajustada, quem recebe R$ {renda}, deverá pagar R$ {ir_reajustado:.2f} de imposto de renda.")


def calcular_ir_sem_reajuste(r):
    taxa_1 = 1903.98
    taxa_2 = 2826.65
    taxa_3 = 3751.05
    taxa_4 = 4664.68

    if r <= taxa_1: 
        return 0
    elif r <= taxa_2:
        r -= taxa_1
        return (7.5 / 100) * r
    elif r <= taxa_3:
        r1 = (7.5 / 100) * (taxa_2 - taxa_1)
        r -= taxa_2
        return ((15 / 100) * r) + r1
    elif r <= taxa_4:
        r1 = (7.5 / 100) * (taxa_2 - taxa_1)
        r2 = (15 / 100) * (taxa_3 - taxa_2)
        r -= taxa_3
        return ((22.5 / 100) * r) + r1 + r2
    else:
        r1 = (7.5 / 100) * (taxa_2 - taxa_1)
        r2 = (15 / 100) * (taxa_3 - taxa_2)
        r3 = (22.5 / 100) * (taxa_4 - taxa_3)
        r -= taxa_4
        return ((27.5 / 100) * r) + r1 + r2 + r3


def calcular_ir_com_reajuste(r):
    taxa_1 = 3881.65
    taxa_2 = 5714.11
    taxa_3 = 7654.67
    taxa_4 = 9564.42

    if r <= taxa_1: 
        return 0
    elif r <= taxa_2:
        r -= taxa_1
        return (7.5 / 100) * r
    elif r <= taxa_3:
        r1 = (7.5 / 100) * (taxa_2 - taxa_1)
        r -= taxa_2
        return ((15 / 100) * r) + r1
    elif r <= taxa_4:
        r1 = (7.5 / 100) * (taxa_2 - taxa_1)
        r2 = (15 / 100) * (taxa_3 - taxa_2)
        r -= taxa_3
        return ((22.5 / 100) * r) + r1 + r2
    else:
        r1 = (7.5 / 100) * (taxa_2 - taxa_1)
        r2 = (15 / 100) * (taxa_3 - taxa_2)
        r3 = (22.5 / 100) * (taxa_4 - taxa_3)
        r -= taxa_4
        return ((27.5 / 100) * r) + r1 + r2 + r3


main()
