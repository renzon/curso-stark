frutas = ['banana', 'maça']

print(type(frutas))
print(frutas)
print(frutas[0])
quantidade_de_frutas = len(frutas)
saida = f'existem {quantidade_de_frutas} fruta(s)'
print(saida)
# print('existem', quantidade_de_frutas, 'fruta(s)', sep='/-/')


numeros = list(range(1, 11))
print(numeros)
letras = list('Stark')
print(letras)
print(*letras, sep='@')
print(letras[0], letras[1], letras[2], letras[3], letras[4], sep='@')
print(letras[-1])

print(frutas)
frutas.append('caqui')
print(frutas)
frutas.append('uva')
print(frutas)
