while True:
    # Fazer lógica de pedir valor entre 0 e 10 para o usuário
    try:
        n = float(input('Digite um número entre 0 e 10: '))
    except ValueError:
        print('Você precisa digitar um valor numérico! Tente novamente.')
    else:
        if 0 <= n <= 10:
            print('Parabéns, colocou um número válido')
            break
        print(f'O valor {n} não está entre 0 e 10. Tente novamente')