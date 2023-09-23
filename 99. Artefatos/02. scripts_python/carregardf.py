import pandas as pd

# Carregar o arquivo CSV em um DataFrame
url = "https://raw.githubusercontent.com/meddavid/Mackenzie-Projeto-Aplicado-I/adf5948da5b4b0f8fc2bee7fa4dad0ac60f23102/99.%20Artefatos/01.%20Dataset/vaccination-data.csv"
df = pd.read_csv(url)

# Mostra um resumo do DataFrame (tipos de dados, não nulos, etc.)
df.info()
#print(df)
