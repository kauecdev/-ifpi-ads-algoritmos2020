def main():
  
  n = int(input("Digite um valor: "))

  # Método com while

  # counter = 1
  # s = 0

  # while counter <= n:
  #   s += (1 / counter)

  #   counter += 1

  # Método com for

  s = 0

  for i in range(1, n + 1):
    s += (1 / i)

  print(f's: {s:.2f}')


main()