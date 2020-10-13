def main():
  ordem_matriz = int(input("Qual a ordem da matriz? "))

  matriz_quadrada = gerar_matriz(ordem_matriz)

  print_matriz(matriz_quadrada)
  calcular_maior_menor(matriz_quadrada)

def calcular_maior_menor(matriz):
  maior = -1
  menor = 99999
  index_maior = -1
  index_menor = -1

  for i in range(len(matriz)):
    sum_of_rows = 0
    for j in range(len(matriz[i])):
      sum_of_rows += matriz[i][j]

    if sum_of_rows > maior:
      maior = sum_of_rows
      index_maior = i + 1
      
    if sum_of_rows < menor:
      menor = sum_of_rows
      index_menor = i + 1

  print(f'A linha com a maior soma de elementos é a linha {index_maior} com total de {maior}.')
  print(f'A linha com a menor soma de elementos é a linha {index_menor} com total de {menor}.')


def gerar_matriz(ordem):
  matriz = []

  criar_vetor(ordem)

  for i in range(ordem):
    matriz.append(criar_vetor(ordem))

  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      matriz[i][j] = int(input(f"Valor a ser inserido em [{i}][{j}]: "))

  return matriz

def criar_vetor(ordem):
  vetor = [0] * ordem
  return vetor

def print_matriz(matriz):
  for row in matriz:
    print(row)

main()