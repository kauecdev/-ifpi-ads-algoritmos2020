def main(): 
  n = int(input("N: "))

  for i in range(n):
    s = input("S: ")
    isfunny(s)


def isfunny(text):
  s = text
  r = text[::-1]
  count = 0

  for i in range(0, len(s) - 1, 1):
    x = difference(s[i + 1], s[i])
    y = difference(r[i + 1], r[i])

    if (x == y):
      count += 1

  if count == (len(text) - 1):
    print("Funny")
  else: 
    print("Not Funny")


def difference(a,b):
  n1 = ord(a)
  n2 = ord(b)

  value = n1 - n2

  if value < 0:
    value *= -1

  return value


main()