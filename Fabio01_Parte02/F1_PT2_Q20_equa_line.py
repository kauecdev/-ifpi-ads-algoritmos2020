#  Entrada

a = int(input("Digite um valor para 'a': "))
b = int(input("Digite um valor para 'b': "))
c = int(input("Digite um valor para 'c': "))
d = int(input("Digite um valor para 'd': "))
e = int(input("Digite um valor para 'e': "))
f = int(input("Digite um valor para 'f': "))

# Processamento

x = ((c * e) - (b * f)) / ((a * e) - (b * d))
y = ((a * f) - (c * d)) / ((a * e) - (b * d))

print(f"A solução para as equações (x = ce - bf / ae - bd) e (y = af - cd / ae - bd) com os valores:", 
f"\na = {a}, b = {b}, c = {c}, d = {d}, e = {e}, f = {f}, é: {x} e {y}.")