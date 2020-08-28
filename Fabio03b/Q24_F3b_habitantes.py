def main():

  n_habitantes = int(input("Digite a quantidade de habitantes: "))

  counter = 0
  salario_total = 0
  numero_filhos = 0
  numero_pessoas_com_salario_ate_mil = 0

  # Método com while

  # while counter < n_habitantes:
  #   salario_habitante = float(input("Digite o salário do habitante: "))
  #   numero_filhos_por_habitante = int(input("Digite o número de filhos que o habitante tem: "))

  #   if salario_habitante <= 1000:
  #     numero_pessoas_com_salario_ate_mil += 1

  #   salario_total += salario_habitante
  #   numero_filhos += numero_filhos_por_habitante

  #   counter += 1

  # Método com for

  for i in range(0, n_habitantes):
    salario_habitante = float(input("Digite o salário do habitante: "))
    numero_filhos_por_habitante = int(input("Digite o número de filhos que o habitante tem: "))

    if salario_habitante <= 1000:
      numero_pessoas_com_salario_ate_mil += 1

    salario_total += salario_habitante
    numero_filhos += numero_filhos_por_habitante

  media_salario = salario_total / n_habitantes
  media_filhos = numero_filhos / n_habitantes
  porcentagem_pessoas_com_salario_ate_mil = (numero_pessoas_com_salario_ate_mil / n_habitantes) * 100

  print(f"\nMédia de salário: R$ {media_salario}\n")
  print(f"Média de filhos: {media_filhos}\n")
  print(f"Porcentagem de pessoas com salário de até R$ 1000,00: {porcentagem_pessoas_com_salario_ate_mil:.2f}%\n")

main()