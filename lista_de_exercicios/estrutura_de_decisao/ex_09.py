numero_1 = float(input('Digite um número: '))
numero_2 = float(input('Digite outro número: '))
numero_3 = float(input('Digite outro número: '))

if numero_3 >= numero_2 >= numero_1:
    print(numero_3, numero_2, numero_1)
elif numero_3 >= numero_1 >= numero_2:
    print(numero_3, numero_1, numero_2)
elif numero_1 >= numero_3 >= numero_2:
    print(numero_1, numero_3, numero_2)
elif numero_1 >= numero_2 >= numero_3:
    print(numero_1, numero_2, numero_3)
elif numero_2 >= numero_1 >= numero_3:
    print(numero_2, numero_1, numero_3)
elif numero_2 >= numero_3 >= numero_1:
    print(numero_2, numero_3, numero_1)
