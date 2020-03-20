def main():
    print("Responda com s (para sim) ou n (para não).")

    pergunta_a = str(input("Telefonou para a vítima? "))
    pergunta_b = str(input("Esteve no local do crime? "))
    pergunta_c = str(input("Mora perto da vítima? "))
    pergunta_d = str(input("Devia para a vítima? "))
    pergunta_e = str(input("Já trabalhou com a vítima? "))

    verificar_suspeito(pergunta_a,pergunta_b,pergunta_c,pergunta_d,pergunta_e)


def verificar_suspeito(a,b,c,d,e):
    concatenar = a + b + c + d + e
    total_s = concatenar.count('s')
    
    if total_s <= 2:
        print("A pessoa é suspeita.")
    elif total_s <= 4:
        print("A pessoa é cúmplice.")
    elif total_s == 5:
        print("A pessoa é o(a) assassino(a).")

    
main()