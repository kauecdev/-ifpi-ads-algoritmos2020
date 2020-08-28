def main():

  print("------ Eleições ------")

  print("Número de voto do Candidato 1 = 1")
  print("Número de voto do Candidato 2 = 2")
  print("Número de voto do Candidato 3 = 3\n")

  print("Código para votos nulos = 9")
  print("Código para votos em branco = 0\n")

  numero_eleitores = int(input("Digite a quantidade de eleitores: "))

  counter = 0

  qtd_votos_primeiro_candidato = 0
  qtd_votos_segundo_candidato = 0
  qtd_votos_terceiro_candidato = 0
  qtd_votos_nulos = 0
  qtd_votos_em_branco = 0

  # Método com while

  # while counter < numero_eleitores:
  #   codigo_voto = int(input("Digite o código do candidato: "))

  #   if codigo_voto == 1:
  #     qtd_votos_primeiro_candidato += 1
  #   elif codigo_voto == 2:
  #     qtd_votos_segundo_candidato += 1
  #   elif codigo_voto == 3:
  #     qtd_votos_terceiro_candidato += 1
  #   elif codigo_voto == 9:
  #     qtd_votos_nulos += 1
  #   elif codigo_voto == 0:
  #     qtd_votos_em_branco += 1
  #   else:
  #     print("Número inválido")

  #   counter += 1

  # Método com for

  for i in range(0, numero_eleitores):
    codigo_voto = int(input("Digite o código do candidato: "))

    if codigo_voto == 1:
      qtd_votos_primeiro_candidato += 1
    elif codigo_voto == 2:
      qtd_votos_segundo_candidato += 1
    elif codigo_voto == 3:
      qtd_votos_terceiro_candidato += 1
    elif codigo_voto == 9:
      qtd_votos_nulos += 1
    elif codigo_voto == 0:
      qtd_votos_em_branco += 1
    else:
      print("Número inválido")


  print(f"\nQuantidade de votos do primeiro candidato: {qtd_votos_primeiro_candidato}")
  print(f"Quantidade de votos do segundo candidato: {qtd_votos_segundo_candidato}")
  print(f"Quantidade de votos do terceiro candidato: {qtd_votos_terceiro_candidato}")
  print(f"Quantidade de votos nulos: {qtd_votos_nulos}")
  print(f"Quantidade de votos em branco: {qtd_votos_em_branco}")

  if qtd_votos_primeiro_candidato > qtd_votos_segundo_candidato and qtd_votos_primeiro_candidato > qtd_votos_terceiro_candidato:
    print("O Primeiro Candidato foi o vencedor das eleições!")
  elif qtd_votos_segundo_candidato > qtd_votos_primeiro_candidato and qtd_votos_segundo_candidato > qtd_votos_terceiro_candidato:
    print("O Segundo Candidato foi o vencedor das eleições!")
  else:
    print("O Terceiro Candidato foi o vencedor das eleições!")

main()