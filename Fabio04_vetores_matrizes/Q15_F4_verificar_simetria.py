def main():
  ordem_matriz = int(input("Qual a ordem da matriz? "))

  matriz_quadrada = gerar_matriz(ordem_matriz)

  print_matriz(matriz_quadrada)

  simetria = verificar_simetria(matriz_quadrada)
  
  if simetria:
    print("É simétrica")
  else:
    print("Não é simétrica")
  
def verificar_simetria(matriz):
  resultado = False

  for i in range(len(matriz)):
    for j in range(len(matriz)):
      if matriz[i][j] == matriz[j][i]:
        resultado = True
      else:
        resultado = False

  return resultado

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