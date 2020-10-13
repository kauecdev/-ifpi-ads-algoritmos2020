def main():
  ordem_matriz = int(input("Qual a ordem da matriz? "))

  matriz_quadrada = gerar_matriz(ordem_matriz)

  print_matriz(matriz_quadrada)
  somar_diagonais(matriz_quadrada)
  somar_outros(matriz_quadrada)

def somar_outros(matriz):
  outros = 0

  for i in range(len(matriz)):
    for j in range(len(matriz)):
      if i != j and ((i + j) != (len(matriz) - 1)):
        outros += matriz[i][j]

  print(f"Soma dos elementos que não estão na matriz principal nem na matriz secundária: {outros}")

def somar_diagonais(matriz):
  diagonal_principal = 0
  diagonal_secundaria = 0

  for i in range(len(matriz)):
    for j in range(len(matriz)):
      if i == j:
        diagonal_principal += matriz[i][j]
      if ((i + j) == (len(matriz) - 1)):
        diagonal_secundaria += matriz[i][j]

  print(f'Soma dos elementos da diagonal principal: {diagonal_principal}\n'
      + f'Soma dos elementos da diagonal secundária: {diagonal_secundaria}'
  )

def print_matriz(matriz):
  for row in matriz:
    print(row)

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


main()
