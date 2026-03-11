import pandas as pd

data = {
    "Nome": ["Manji", "Magatsu", "Musashi", "Guts"],
    "Idade": [251, 25, 31,27],
    "Cidade": ["Edo", "Osaka", "Miyamoto", "Indaial"]
}

df = pd.DataFrame(data)

print(df)

print(df['Nome'])

# Acessando uma linha
print(df.iloc[0])

# Acessar um valor específico
print(df.loc[0, 'Nome'])