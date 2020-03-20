def main():
    x1 = int(input("Coordenada x1: "))
    y1 = int(input("Coordenada y1: "))

    x2 = int(input("Coordenada x2: "))
    y2 = int(input("Coordenada y2: "))

    x1_calculavel = valor_x1_positivo(x1)
    y1_calculavel = valor_y1_positivo(y1)
    x2_calculavel = valor_x2_positivo(x2)
    y2_calculavel = valor_y2_positivo(y2)

    area_retangulo = ((x1_calculavel + x2_calculavel) * (y1_calculavel + y2_calculavel))

    print(f"A área do retângulo é {area_retangulo}(cm²/m²).")


def valor_x1_positivo(x_1):
    if x_1 < 0:
        x_1 *= -1
        return x_1
    else: 
        return x_1


def valor_y1_positivo(y_1):
    if y_1 < 0:
        y_1 *= -1
        return y_1
    else: 
        return y_1


def valor_x2_positivo(x_2):
    if x_2 < 0:
        x_2 *= -1
        return x_2
    else: 
        return x_2


def valor_y2_positivo(y_2):
    if y_2 < 0:
        y_2 *= -1
        return y_2
    else: 
        return y_2


main()