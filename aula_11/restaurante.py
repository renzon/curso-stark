import pandas as pd

# url='https://raw.githubusercontent.com/pandas-dev/pandas/main/pandas/tests/io/data/csv/tips.csv'

df=pd.read_csv('tips.csv')

df.to_excel('tips.xlsx')

print(df)