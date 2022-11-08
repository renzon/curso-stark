def calcular_media(*notas):
    soma = 0
    for nota in notas:
        soma += nota

    return soma / len(notas)


if __name__ == '__main__':
    media = calcular_media(3, 4, 3, 3)
    print(media)

    media = calcular_media(4)
    print(media)
