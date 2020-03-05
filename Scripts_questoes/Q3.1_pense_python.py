def right_justify(s):
    espacos = 70 - len(s)
    justify = (espacos * ' ') + s
    print(justify)

right_justify('questao 3') 