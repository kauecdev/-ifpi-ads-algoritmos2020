def main():
  
  n = int(input("Digite um valor: "))

  counter = 1
  divisor = 1
  dividendo = 1
  s = 0

  while counter <= n:
    s += (divisor / counter)

    divisor += 2
    counter += 1


  print(f's: {s:.2f}')


main()