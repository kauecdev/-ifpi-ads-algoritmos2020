def main():

  quantidade_funcionarios = int(input("Digite a quantidade de funcionários na empresa: "))

  counter = 0

  valor_hora = 12
  valor_dependentes = 40
  taxa_inss = 0.085
  taxa_ir = 0.05

  # Método com while

  # while counter < quantidade_funcionarios:
  #   n_ficha = int(input("Digite o número da ficha: "))
  #   n_horas = int(input("Digite a quantidade de horas trabalhadas: "))
  #   n_dependentes = int(input("Digite o número de dependentes: "))
    
  #   salario_bruto = (n_horas * valor_hora) + (n_dependentes * valor_dependentes)
  #   salario_menos_inss = salario_bruto * taxa_inss
  #   salario_menos_ir = salario_bruto * taxa_ir

  #   salario_liquido = salario_bruto - (salario_menos_inss + salario_menos_ir) 

  #   print(f"\nInformações do funcionário de ficha número: {n_ficha}\n")
  #   print(f"Salário bruto: R$ {salario_bruto:.2f};")
  #   print(f"Taxa do INSS sobre o salário bruto: R$ {salario_menos_inss:.2f};")
  #   print(f"Taxa do IR sobre o salário bruto: R$ {salario_menos_ir:.2f};")
  #   print(f"Salário líquido: R$ {salario_liquido:.2f};\n")

  #   counter += 1

  # Método com for

  for i in range(0, quantidade_funcionarios):
    n_ficha = int(input("Digite o número da ficha: "))
    n_horas = int(input("Digite a quantidade de horas trabalhadas: "))
    n_dependentes = int(input("Digite o número de dependentes: "))
    
    salario_bruto = (n_horas * valor_hora) + (n_dependentes * valor_dependentes)
    salario_menos_inss = salario_bruto * taxa_inss
    salario_menos_ir = salario_bruto * taxa_ir

    salario_liquido = salario_bruto - (salario_menos_inss + salario_menos_ir) 

    print(f"\nInformações do funcionário de ficha número: {n_ficha}\n")
    print(f"Salário bruto: R$ {salario_bruto:.2f};")
    print(f"Taxa do INSS sobre o salário bruto: R$ {salario_menos_inss:.2f};")
    print(f"Taxa do IR sobre o salário bruto: R$ {salario_menos_ir:.2f};")
    print(f"Salário líquido: R$ {salario_liquido:.2f};\n")

main()