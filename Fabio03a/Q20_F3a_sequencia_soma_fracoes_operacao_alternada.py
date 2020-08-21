def main():
  
  n = int(input("Digite um valor: "))

  counter = 1
  s = 0

  while counter <= n:
    if counter % 2 != 0:
      s += (1 / counter)
    else:
      s -= (1 / counter)
      

    counter += 1


  print(f's: {s:.2f}')


main()