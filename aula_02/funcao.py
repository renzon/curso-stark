def calcular_media(nota_1, nota_2, nota_3, nota_4):
    return (nota_1 + nota_2 + nota_3 + nota_4) / 4


if __name__ == '__main__':
    media = calcular_media(3, 4, 3, 3)
    print(media)

    media = calcular_media(4, 10, 10, 10)
    print(media)
