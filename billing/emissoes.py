import pandas as pd

df_original = pd.read_csv('emissoes.csv')

# Removendo colunas desnecessárias
df = df_original.drop('companyTaxId', axis=1).drop('HolmesCreatedFee (R$)', axis=1).drop('companyName', axis=1).drop(
    'workspaceUsername', axis=1)

# Renomeando colunas
df.rename(
    columns={'workspaceId': 'WORKSPACE_ID', 'HolmesCreatedFee (R$).1': 'AMOUNT'},
    inplace=True
)

inicio = '31/10/2022'
fim = '29/11/2022'


def gerar_texto(amount):
    return f'Tarifa por {amount} conta(s) ativa(s) de {inicio} a {fim}'


df['DESCRIPTION'] = df['Record Count'].transform(gerar_texto)

df.drop('Record Count', axis=1, inplace=True)

df.to_excel('emissoes.xlsx', index=False)

print(df_original)
print(df)
