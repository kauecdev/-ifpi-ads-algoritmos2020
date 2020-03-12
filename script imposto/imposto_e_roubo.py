def main():
    renda = float(input("Digite sua renda R$: "))

    taxa = calcular_imposto(renda)
    imposto = renda * (taxa/100)

    print(f"Você será tributado em {taxa}% de taxa.")
    print(f"Logo, pagará R${imposto} em imposto.")

def calcular_imposto(renda):
    if renda <= 1900:
        return 0
    elif renda <= 3000:
        return 14
    elif renda <= 8000:
        return 22
    else:
        return 27

main()