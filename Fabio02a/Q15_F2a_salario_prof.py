def main():
    horas_aula_prof1 = int(input("Digite a sua quantidade de horas aula, professor 1: "))
    horas_aula_prof2 = int(input("Digite a sua quantidade de horas aula, professor 2: "))

    valor_por_hora_prof1 = float(input("Digite o valor que recebe por hora, professor 1: "))
    valor_por_hora_prof2 = float(input("Digite o valor que recebe por hora, professor 2: "))

    salário_prof1 = horas_aula_prof1 * valor_por_hora_prof1
    salário_prof2 = horas_aula_prof2 * valor_por_hora_prof2

    verificar_maior_salário(salário_prof1,salário_prof2)

def verificar_maior_salário(a,b):
    if a > b:
        print("O primeiro professor recebe um salário total maior que o segundo.")
    else: 
        print("O segundo professor recebe um salário total maior que o primeiro.")


main()