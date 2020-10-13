def main():
  vetor = []

  while True:
    num = input("Digite um número de oito dígitos em base binária: ")

    if len(num) == 8 and isBinary(num):
      for i in range(len(num)):
        vetor.append(int(num[i]))
      break
    else:
      print("O número digitado não contém 8 digitos ou algum dígito não corresponde as valores da base binária (0 e 1).")

  converter_bases(vetor)

def converter_bases(vetor):
  grupo_bits_a = vetor[:4]
  grupo_bits_b = vetor[4:]

  first_nibble_hex = bin_to_hex(grupo_bits_a)
  second_nibble_hex = bin_to_hex(grupo_bits_b)

  num_hex = str(first_nibble_hex) + str(second_nibble_hex)

  num_dec = bin_to_dec(vetor)

  print(f'Número digitado em base hexadecimal: {num_hex}\nNúmero digitado em base decimal: {num_dec}.')

def bin_to_dec(vetor):
  num = 0
  num_inverted = vetor[::-1]

  for i in range(len(num_inverted)):
    if num_inverted[i] == 1:
      result = num_inverted[i] * (2 ** i)
      num += result
    
  return num

def bin_to_hex(vetor):
  num = 0

  if vetor[3] == 1:
    num += 1

  if vetor[2] == 1:
    num += 2

  if vetor[1] == 1:
    num += 4

  if vetor[0] == 1:
    num += 8

  if num == 10:
    return 'A'
  elif num == 11:
    return 'B'
  elif num == 12:
    return 'C'
  elif num == 13:
    return 'D'
  elif num == 14:
    return 'E'
  elif num == 15:
    return 'F'

  return num

def isBinary(num):
  num_int = []

  for i in range(len(num)):
    num_int.append(int(num[i]))
  
  for value in num_int:
    if value != 0 and value != 1:
      return False

  return True

main()