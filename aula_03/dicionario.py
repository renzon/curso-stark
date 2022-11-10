moedas = {'BR': 'BRL', 'EUA': 'USD', 'PT': 'EUR', 'FR': 'EUR'}

print('#### Acessos a valores via colchete e chave')
print(moedas['BR'])
print(moedas['EUA'])
print(moedas['PT'])
print(moedas['FR'])

print('#### conjuntos de chaves')
print('Chaves', moedas.keys())
es_esta_no_dicionario = 'ES' in moedas
print('ES está no dicionário? Resposta:', es_esta_no_dicionario)
if es_esta_no_dicionario:  # Preciso perguntar se existe, se não, dá KeyError
    print(moedas['ES'])

print('BR está no dicionário? Resposta:', 'BR' in moedas)

print('#### acesso com função get')
print(moedas.get('BR', 'Moeda não cadastrada'))  # retona o valor BRL porque chave existe em moedas
print(moedas.get('ES', 'Moeda não cadastrada'))  # retona o valor Moeda não cadastrada porque chave não existe em moedas

print('##### Iterando sobre chaves')

for pais in moedas:
    print(pais)

print('##### Iterando sobre items')

for pais, moeda in moedas.items():
    print(f'A moeda de {pais} é {moeda}')
