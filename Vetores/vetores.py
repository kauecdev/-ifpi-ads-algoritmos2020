def main():
  tamanho_vetor = int(input("Quantos números pretende digitar? "))

  vetor = [-1] * tamanho_vetor

  for i in range(len(vetor)):
    vetor[i] =  float(input("Digite um número: "))

  print("\n### VETOR INICIAL ###\n" \
      + f"{vetor}\n"
      + f"Números pares: {numeros_pares(vetor)}\n" \
      + f"Números ímpares: {numeros_impares(vetor)}\n" \
      + f"Números positivos: {numeros_positivos(vetor)}\n" \
      + f"Números negativos: {numeros_negativos(vetor)}\n" \
      )

  for i in range(len(vetor)):
    if vetor[i] >= 0:
      vetor[i] = vetor[i] * 2
    else:
      vetor[i] = vetor[i] / 2

  print("\n### VETOR  TRANSFORMADO ###\n" \
      + f"{vetor}\n"
      + f"\nNúmeros pares: {numeros_pares(vetor)}\n" \
      + f"Números ímpares: {numeros_impares(vetor)}\n" \
      + f"Números positivos: {numeros_positivos(vetor)}\n" \
      + f"Números negativos: {numeros_negativos(vetor)}\n" \
      )

  print(f"A média dos valores do vetor transformado é: {media_valores_vetor(vetor)}")


def numeros_pares(vetor):
  qtd_numeros_pares = 0
  
  for num in vetor:
    if num % 2 == 0:
      qtd_numeros_pares += 1
    
  return qtd_numeros_pares


def numeros_impares(vetor):
  qtd_numeros_impares = 0
  
  for num in vetor:
    if num % 2 != 0:
      qtd_numeros_impares += 1

  return qtd_numeros_impares


def numeros_positivos(vetor):
  qtd_numeros_positivos = 0
    
  for num in vetor:
    if num >= 0:
      qtd_numeros_positivos += 1

  return qtd_numeros_positivos


def numeros_negativos(vetor):
  qtd_numeros_negativos = 0
    
  for num in vetor:
    if num < 0:
      qtd_numeros_negativos += 1

  return qtd_numeros_negativos


def media_valores_vetor(vetor):
  acumulador = 0

  for i in range(len(vetor)):
    acumulador += vetor[i]

  media_valores = acumulador / len(vetor)

  return media_valores


main()