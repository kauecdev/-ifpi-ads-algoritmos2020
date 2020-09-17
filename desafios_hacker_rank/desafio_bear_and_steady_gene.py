def main():
  n = int(input("N: "))

  if n >= 4 and (n % 4) == 0:
    gene = input()

    print(steady_gene(gene))

  else:
    print("O tamanho do gene deve ser múltiplo de 4.")


def steady_gene(gene):
  genes = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
  for i in gene:
    genes[i] += 1

  len_gene = len(gene)
  min_frequency = len_gene / 4

  # Verificamos inicialmente se todos os caracteres digitados correspondem a 1/4 (um quarto) da string.

  if genes['A'] == min_frequency and genes['T'] == min_frequency and genes['C'] == min_frequency and genes['G'] == min_frequency:
    return 0

  low = 0
  high = 0
  min_len = len_gene

  # Caso não, passamos por um loop onde iremos checar e ajustar a quantidade correta para estabilizar o gene.

  while high < len_gene and low < len_gene:
    while (genes['A']) > min_frequency or (genes['T']) > min_frequency or (genes['C']) > min_frequency or (genes['G']) > min_frequency and high < len_gene:
      genes[gene[high]] -= 1
      high += 1

    while (genes['A']) <= min_frequency and (genes['T']) <= min_frequency and (genes['C']) <= min_frequency and (genes['G']) <= min_frequency:
      genes[gene[low]] += 1
      low += 1
    
    if high - low < min_len:
      min_len = high - low + 1

  return min_len


main()