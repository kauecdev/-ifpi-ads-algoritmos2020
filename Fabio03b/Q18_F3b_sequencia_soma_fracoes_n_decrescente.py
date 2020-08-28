def main():
  
  n = int(input("Digite um valor: "))

  # Método com while

  # counter = 1
  # decrescentador = n
  # s = 0

  # while counter <= n:
  #   s += (counter / decrescentador)

  #   decrescentador -= 1
  #   counter += 1

  # s += (n / 1)

  # Método com for

  decrescentador = n
  s = 0

  for i in range(1,n + 1):
    s += (i / decrescentador)

    decrescentador -= 1

  s += (n / 1)

  print(f's: {s:.2f}')


main()