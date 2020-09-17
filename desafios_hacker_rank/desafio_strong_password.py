def main():
  n = int(input("Tamanho da senha: "))

  password = input("Senha: ")

  if len(password) > n or len(password) < n:
    print("A senha digitada contém mais caracteres ou menos caracteres que quantidade que você digitou inicialmente.")
    return

  verificar_senha(password)
 

def verificar_senha(password):
  has_numbers = verificar_numeros(password)
  has_lower_case = verificar_letras_minusculas(password)
  has_upper_case = verificar_letras_maiusculas(password)
  has_special_characters = verificar_caracteres_especiais(password)

  problems = 0

  print(f"Contém números? {has_numbers}\nContém letras minúsculas? {has_lower_case}\nContém letras maiúsculas? {has_upper_case}\nContém caracteres especiais? {has_special_characters}")

  if len(password) < 6:
    print(6 - len(password))
    return
  elif has_numbers and has_lower_case and has_upper_case and has_special_characters:
    print(problems)
    return
  elif not(has_numbers) or not(has_lower_case) or not(has_upper_case) or not(has_special_characters):
    problems += 1

  print(problems)


def verificar_numeros(password):
  verificacao = False

  for character in password:
    if ord(character) >= 48 and ord(character) <= 57:
      verificacao = True

  return verificacao

def verificar_letras_minusculas(password):
  verificacao = False

  for character in password:
      if ord(character) >= 97 and ord(character) <= 122:
        verificacao = True

  return verificacao

def verificar_letras_maiusculas(password):
  verificacao = False

  for character in password:
      if ord(character) >= 65 and ord(character) <= 90:
        verificacao = True

  return verificacao


def verificar_caracteres_especiais(password):
  verificacao = False
  
  for character in password:
    if isspecial_character(character):
      return True

  return verificacao

def isspecial_character(character):
  special_characters = "!@#$%^&*()-+"

  for i in range(len(special_characters)):
    if character == special_characters[i]:
      return True

main()