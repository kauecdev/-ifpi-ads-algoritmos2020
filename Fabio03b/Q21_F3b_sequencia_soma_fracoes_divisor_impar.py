def main():
  
  n = int(input("Digite um valor: "))

  # Método com while

  # counter = 1
  # divisor = 1
  # dividendo = 1
  # s = 0

  # while counter <= n:
  #   s += (divisor / counter)

  #   divisor += 2
  #   counter += 1

  # Método com for

  divisor = 1
  dividendo = 1
  s = 0

  for i in range(1, n + 1):
    s += (divisor / i)

    divisor += 2

  print(f's: {s:.2f}')


main()