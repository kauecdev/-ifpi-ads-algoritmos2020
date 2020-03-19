def main():
    nota_1 = float(input("Digite sua primeira nota (entre 0 e 10): "))
    nota_2 = float(input("Digite sua segunda nota (entre 0 e 10): "))

    verificar_media(nota_1,nota_2)
    

def verificar_media(a,b):
    media = (a + b) / 2
    if media >= 7:
        print("Aprovado")
    elif media < 7:
        print("Reprovado.")
        prova_final = float(input("Digite a nota da sua prova final (entre 0 e 10): "))
        media_final = ((prova_final + media) / 2)
        if media_final >= 5:
            print("Aprovado.")
        else: 
            print("Reprovado.")
   


main()