def main():
  
  qtd_fichas = int(input("Digite a quantidade de fichas a registrar: "))

  counter = 0
  boi_mais_magro = 99999
  boi_mais_gordo = 0
  n_ficha_magro = 0
  n_ficha_gordo = 0

  while counter < qtd_fichas:
    nova_ficha = int(input("Digite o número da ficha do boi: "))
    peso_boi = int(input("Digite o peso do boi: "))

    if peso_boi > boi_mais_gordo:
      n_ficha_gordo = nova_ficha
      boi_mais_gordo = peso_boi

    if peso_boi < boi_mais_magro:
      n_ficha_magro = nova_ficha
      boi_mais_magro = peso_boi

    counter += 1

  print(f"\nO boi mais gordo tem número de identificação {n_ficha_gordo} e pesa {boi_mais_gordo} Kg.")
  print(f"Já o boi mais magro tem número de identificação {n_ficha_magro} e pesa {boi_mais_magro} Kg.")

main()

