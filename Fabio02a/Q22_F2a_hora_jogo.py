def main():
    print("Os horários devem ser digitados no formato 24hr.")
    
    hora_inicio = int(input("Digite a hora do inicio do jogo: "))
    minutos_inicio = int(input("Digite os minutos do inicio do jogo: "))
    hora_final = int(input("Digite a hora do término do jogo: "))
    minutos_final = int(input("Digite os minutos do término do jogo: "))
    
    resultado(hora_inicio, minutos_inicio, hora_final, minutos_final)


def resultado(hi, mi, hf, mf):
    hora_termino = hf - hi
    minuto_termino = mf - mi


    if minuto_termino < 0:
        minuto_termino = (minuto_termino / 60) * (-1)


    if hora_termino < 0:
        dif = 24 - hi
        hora_termino = hf + dif
    hora_termino = hora_termino - minuto_termino
    minuto_termino = (hora_termino % 1) * 60
    hora_termino = hora_termino // 1 


    if hora_termino <= 24:
        print(f"O horário do jogo completo foi de: {hora_termino}hr {minuto_termino}min")

        
    else:
        print(f"O jogo não pode acontecer por mais de 24h")


main()