numeros = []

for i in range(3):
    numero = float(input('Digite um número: '))
    numeros.append(numero)

print(numeros)

numeros.sort(reverse=True)

print(numeros)
