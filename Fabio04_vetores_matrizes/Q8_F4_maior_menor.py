def main():
  qtd_elementos = int(input("Digite a quantidade de elementos a adicionar no vetor: "))

  vetor = []

  for i in range(qtd_elementos):
    item = int(input("Digite um valor: "))

    vetor.append(item)

  verificar_maior_menor(vetor)


def verificar_maior_menor(vetor):
  maior = 0
  menor = 99999

  for item in vetor:
    if item > maior:
      maior = item

    if item < menor:
      menor = item

  pos_maior = index(maior, vetor)
  pos_menor = index(menor, vetor)

  print(f"Maior número: {maior}, posição no vetor: {pos_maior}\nMenor número: {menor}, posição no vetor: {pos_menor}")


def index(num, vetor):
  for i in range(len(vetor)):
    if vetor[i] == num:
      return i

main()