def main():
  s = input("S: ")

  if not(ismultiple_of_three(s)):
    print("O texto digitado deve conter somente a mensagem SOS.")
    return

  verify_message(s)


def verify_message(message):
  number_of_messages = len(message) // 3

  invalid_characters = 0

  for j in range (0, len(message), 3):
    if sos_message(message[j:j+3:1]):
      pass
    else:
      invalid_characters += verify_invalid_character(message[j:j+3:1])

  print(invalid_characters)


def sos_message(message):
  if message == 'SOS':
    return True
  else:
    return False

def verify_invalid_character(message):
  invalid_characters = 0

  if message[0] != 'S' or message[2] != 'S':
    invalid_characters += 1
  
  if message[1] != 'O':
    invalid_characters +=1

  return invalid_characters

def ismultiple_of_three(s):
  if len(s) % 3 == 0:
    return True
  else:
    return False

main()