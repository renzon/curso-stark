numeros = list(range(1, 10))

print(numeros)

print('#### Imprimindo elementos linha a linha')
for qualquer_coisa in numeros:
    print(qualquer_coisa)


print('#### Criar segunda lista com valores da primeira elevados ao quadrado')

numeros_ao_quadrado = []

for numero in numeros:
    numeros_ao_quadrado.append(numero ** 2)

print(numeros_ao_quadrado)

print(sum(numeros[:4]))

print(9 in numeros)
print(-1 in numeros)
