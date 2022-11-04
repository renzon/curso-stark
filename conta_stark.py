idade_str = input('Bem vindo ao Stark Bank. Digite sua idade: ')
idade = int(idade_str)

if idade >= 18:
    print('Pode abrir conta na Stark')
    tipo_conta = input('Digite 1 para abrir uma conta PF ou 2 para PJ: ')
    if tipo_conta == '1':
        print('Parabéns, sua conta PF foi aberta')
    else:
        print('Parabéns, sua conta PJ foi aberta')
elif idade <= 2:
    print('Como um bebe consegue digitar?')
else:
    print('Não Pode abrir conta na Stark')