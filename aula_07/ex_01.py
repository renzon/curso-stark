while True:
    # Fazer lógica de pedir valor entre 0 e 10 para o usuário
    n = float(input('Digite um número entre 0 e 10: '))

    if 0 <= n <= 10:
        break

    print(f'O valor {n} não está entre 0 e 10. Tente novamente')