numeros = list(range(3))

for numero in numeros:
    print(numero)

print('### Execução do while')
indice = 0
tamanho_da_lista = len(numeros)
while True:  # tamanho_da_lista = 3 indice=2
    valor = numeros[indice]
    print(valor)
    indice += 1
    if indice == tamanho_da_lista:
        break

print('### Terminou o programa')
