import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

print(df['Age'])  # Acesso à Coluna Age
print(df['Age'][1])  # Acesso à segunda célula da Coluna Age

print('######## Describe')
print(df['Age'].describe())  # Acesso à segunda célula da Coluna Age
