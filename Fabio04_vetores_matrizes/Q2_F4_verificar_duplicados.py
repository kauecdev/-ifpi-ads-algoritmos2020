def main():
  qtd_el = int(input("Quantos itens deseja adicionar ao vetor? "))
  a = []

  for i in range(qtd_el):
    num = int(input("Item: "))
    a.append(num)

  verificar_iguais(a)


def verificar_iguais(seq):
  lista_sem_duplicados = []

  for i in seq:
    if i not in lista_sem_duplicados:
      lista_sem_duplicados.append(i)

  if len(seq) != len(lista_sem_duplicados):
    print("Existem elementos duplicados na lista.")
  else:
    print("Não existem elementos duplicados na lista.")


main()