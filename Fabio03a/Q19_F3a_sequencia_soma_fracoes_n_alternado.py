def main():
  
  n = int(input("Digite um valor: "))

  counter = 1
  decremento = n
  s = 0

  while counter <= n:
    if counter % 2 != 0:
      s += (counter / decremento)
    else: 
      s -= (decremento / counter)
      

    decremento -= 1
    counter += 1

  s += (n / 1)

  print(f's: {s:.2f}')


main()