import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('Ice Cream Sales - temperatures.csv')

from IPython.display import display

sorted_df = df.sort_values(by='Temperature', ascending=True)
display(sorted_df)

# Agora você pode escrever qualquer coisa aqui embaixo que a tabela continuará lá em cima!
print("Ordenação concluída com sucesso!")
