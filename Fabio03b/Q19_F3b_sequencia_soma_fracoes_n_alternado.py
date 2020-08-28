def main():
  
  n = int(input("Digite um valor: "))

  # Método com while

  # counter = 1
  # decremento = n
  # s = 0

  # while counter <= n:
  #   if counter % 2 != 0:
  #     s += (counter / decremento)
  #   else: 
  #     s -= (decremento / counter)
      

  #   decremento -= 1
  #   counter += 1

  # s += (n / 1)

  # Método com for

  decremento = n
  s = 0

  for i in range(1, n + 1):
    if i % 2 != 0:
      s += (i / decremento)
    else: 
      s -= (decremento / i)

    decremento -= 1

  s += (n / 1)

  print(f's: {s:.2f}')


main()