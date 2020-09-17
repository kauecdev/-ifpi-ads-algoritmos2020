def main():
  n = int(input("N: "))
  
  for i in range(n):
    s = input("S: ")

    check_anagrams(s)
  

def check_anagrams(s):
  anagrams = 0
  len_s = len(s)

  for i in range(1, len_s): # Percorremos todos os caracteres da string

    list_substrings = {} # O dicionário fica dentro do laço para a cada vez que for percorrido, ter seu valor zerado e assim, ser possível a contagem do total de anagramas.

    for j in range(len_s - i + 1):
      substring = ''.join(sorted(s[j:j+i])) # Adicionamos todas as substrings possíveis no dicionário para contabilizar suas possibilidades
      

      if substring not in list_substrings: # Verificamos se a substring esta na listra. Caso não esteja, inicializamos seu valor em 1, caso esteja, somamos mais 1.

        list_substrings[substring] = 1
      else:
        list_substrings[substring] += 1

      anagrams += list_substrings[substring] - 1

  print(list_substrings[substring])


main()