import pandas as pd

data = {
    'Nome': ["Manji", "Magatsu", "Musashi", "Guts"],
    'Endereço': ['Perto do ribeirão, sem número, Edo', 'Pousada da Keiko, 11, Edo', 'Templo Takuan, 123, Miyamoto', 'Av. Getúlio Vargas, 126, Indaial'],
    'Data de nascimento': ['02/01/1979', '09/03/1983', '19/04/1965', '10/10/1981'],
    'Data de admissão': ['02/02/2015', '11/05/2019', '28/03/2011', '05/11/2004'],
    'Salário': ['R$ 2.800', 'R$ 2.300', 'R$ 6.550', 'R$ 2.100'],
    'Cargo': ['Segurança', 'Auxiliar de produção', 'Gerente de RH', 'Operador de máquina I']
}

df = pd.DataFrame(data)
print(df)

# --- DICA PROFISSIONAL 1: LIMPEZA DE STRING PARA NUMÉRICO ---
# Removemos o 'R$ ' e o ponto '.', depois convertemos para float
df['Salário_Numerico'] = df['Salário'].str.replace('R$ ', '', regex=False).str.replace('.', '', regex=False).astype(float)

# --- DICA PROFISSIONAL 2: CONVERSÃO PARA DATETIME ---
# Transformamos texto em "objeto de data" real para cálculos de tempo
df['Data de admissão'] = pd.to_datetime(df['Data de admissão'], dayfirst=True)

# --- ANÁLISE DOS DADOS ---
total_folha = df['Salário_Numerico'].sum()
media_salarial = df['Salário_Numerico'].mean()

print("--- Tabela Processada ---")
print(df[['Nome', 'Data de admissão', 'Salário_Numerico']])
print(f"\nTotal da Folha de Pagamento: R$ {total_folha:,.2f}")
print(f"Média Salarial: R$ {media_salarial:,.2f}")

# --- DICA PROFISSIONAL 3: DIAGNÓSTICO DE TIPOS ---
print("\n--- Diagnóstico de Tipos de Dados (Dtypes) ---")
print(df.info())



print(df['Data de admissão'])
