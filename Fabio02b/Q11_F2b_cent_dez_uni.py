def main():
    numero = int(input("Digite um número menor que 1000: "))

    centenas = numero // 100
    resto_div_c = numero % 100
    dezenas = resto_div_c // 10
    unidades = resto_div_c % 10
    
    c = verificar_centenas(centenas)
    d = verificar_dezenas(dezenas)
    u = verificar_unidades(unidades)

    resultado(centenas,dezenas,unidades,c,d,u)

def verificar_centenas(c):
    if c == 1: 
        return "1 centena"
    else:
        return f"{c} centenas"


def verificar_dezenas(d):
    if d == 1: 
        return "1 dezena"
    else:
        return f"{d} dezenas"


def verificar_unidades(u):
    if u == 1: 
        return "1 unidade"
    else:
        return f"{u} unidades"


def resultado(cent,dez,uni,c,d,u):
    if cent >= 1 and dez >= 1 and uni >= 1:
        print(f"{c}, {d} e {u}.")
    elif cent >= 1 and dez >= 1 and uni == 0:
        print(f"{c} e {d}.")
    elif cent >= 1 and dez == 0 and uni >=1:
        print(f"{c} e {u}.")
    elif cent == 0 and dez >= 1 and uni >= 1:
        print(f"{d} e {u}.")
    elif cent == 0 and dez == 0 and uni >= 1:
        print(f"{u}.")
    
    

main()