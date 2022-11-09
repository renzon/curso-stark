'''
Dada a variável nome, imprimir todas as letras e sua posição na string.

Exemplo:
String "Dia", o programa deve imprimir

0 - D
1 - i
2 - a

'''

s = 'Stark Bank'
indice = 0

for letra in s:
    print(indice, '-', letra)
    indice += 1

print('##### Forma elegante de fazer o mesmo que o código acima')

for indice, letra in enumerate(s):
    print(indice, '-', letra)

