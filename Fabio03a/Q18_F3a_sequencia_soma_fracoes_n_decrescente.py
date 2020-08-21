def main():
  
  n = int(input("Digite um valor: "))

  counter = 1
  decrescentador = n
  s = 0

  while counter <= n:
    s += (counter / decrescentador)

    decrescentador -= 1
    counter += 1

  s += (n / 1)

  print(f's: {s:.2f}')


main()