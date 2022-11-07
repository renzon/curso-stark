nome = 'Stark Bank'

print(nome[0])
print('###### Início do for')
for qualquer_coisa in nome:
    print(qualquer_coisa)
print('###### Fim do for')


print(nome[:5])

print('###### Início do split')
primeira_palavra, segunda_palavra = nome.split()
print(primeira_palavra)
print(segunda_palavra)