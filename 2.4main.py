import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('titanic.csv')

print(df.head())

print(df.info())

print(df.describe())

# Datatypes
print(df.dtypes)

# Filtro
print(df[df['age'] <= 10].head())

duplicateRows = df[df.duplicated()]
print(len(duplicateRows))

print(len(df))
df.drop_duplicates(keep='last', inplace=True)
print(len(df))

#df.dropna(subset=['deck'], inplace=True)

# Substituindo NaN por zero
df.replace(np.nan, '0', inplace=True)
print(df)

# Renomear colunas
df = df.rename(columns={'sex': 'Gender'})
print(df.head(5))

sorted_df = df.sort_values(by='Gender', ascending=True)

print(sorted_df)

# Groupby
grouped_by = df.groupby('age')

print(grouped_by.head())