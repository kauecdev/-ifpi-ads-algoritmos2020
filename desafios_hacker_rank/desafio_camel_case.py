def main():
  s = input()

  count_words(s)


def count_words(text):
  count = 0
  first_character = text[0]

  for i in range(0, len(text)):
    if i == 0 and isalpha(first_character) and islower(first_character):
      count += 1
    elif not(isalpha(first_character)):
      print("O primeiro caractere deve ser alfabético.")
      break
    elif not(islower(first_character)):
      print("A primeira palavra deve estar em minúsculo.")
      break
    elif isalpha(text[i]) and isupper(text[i]):
      count += 1

  print(count)


def isalpha(text):
  for char in text:
    if (ord(char) >= 65 and ord(char) <= 89) or (ord(char) >= 97 and ord(char) <= 122):
      return True
    else:
      return False

def isupper(character):
  if (ord(character) >= 65 and ord(character) <= 90):
    return True
  else:
    return False

def islower(character):
  if (ord(character) >= 97 and ord(character) <= 122):
    return True
  else:
    return False

main()