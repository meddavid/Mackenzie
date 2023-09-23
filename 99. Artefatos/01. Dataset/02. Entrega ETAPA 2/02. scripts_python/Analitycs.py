import pandas as pd

# Carregar o DataFrame do github

url = "https://raw.githubusercontent.com/meddavid/Mackenzie-Projeto-Aplicado-I/adf5948da5b4b0f8fc2bee7fa4dad0ac60f23102/99.%20Artefatos/01.%20Dataset/vaccination-data.csv"
dados = pd.read_csv(url)


# Analisando Quantidade de Registros
num_registros = len(dados)
print(f"#### - Quantidade de registros: {num_registros}\n")

# Analisando Quantidade de registros agrupados por WHO_REGION
grupos = dados.groupby('WHO_REGION')
num_registros_por_grupo = grupos.size()
print(" Quantidade de registros agrupados por WHO_REGION:")
print(num_registros_por_grupo)
print("\nGrupos formados:")
print(list(grupos.groups.keys()))
print()

# Analisando colunas numéricas
colunas_numericas = [
    'TOTAL_VACCINATIONS',
    'PERSONS_VACCINATED_1PLUS_DOSE',
    'TOTAL_VACCINATIONS_PER100',
    'PERSONS_VACCINATED_1PLUS_DOSE_PER100',
    'PERSONS_LAST_DOSE',
    'PERSONS_LAST_DOSE_PER100',
    'NUMBER_VACCINES_TYPES_USED',
    'PERSONS_BOOSTER_ADD_DOSE',
    'PERSONS_BOOSTER_ADD_DOSE_PER100'
]

for coluna in colunas_numericas:
    print(f"Análise da coluna '{coluna}':")

    # Número de registros
    num_registros_coluna = dados[coluna].count()
    print(f"Número de registros: {num_registros_coluna}")

    # Valor Máximo
    valor_maximo = dados[coluna].max()
    print(f"Valor Máximo: {valor_maximo:.2f}")

    # Valor Mínimo
    valor_minimo = dados[coluna].min()
    print(f"Valor Mínimo: {valor_minimo:.2f}")

    # Variância
    variancia = dados[coluna].var()
    print(f"Variância: {variancia:.2f}")

    # Desvio Padrão
    desvio_padrao = dados[coluna].std()
    print(f"Desvio Padrão: {desvio_padrao:.2f}")

    # Distribuição
    distribuicao = dados[coluna].describe().apply(lambda x: f'{x:.2f}')
    print(f"Distribuição:\n{distribuicao}")

    # Quantidade de NAs (dados faltantes)
    quantidade_nas = dados[coluna].isna().sum()
    print(f"Quantidade de NAs (dados faltantes): {quantidade_nas:.2f}")

    # Identificar outliers
    Q1 = dados[coluna].quantile(0.25)
    Q3 = dados[coluna].quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    outliers = dados[(dados[coluna] < limite_inferior) | (dados[coluna] > limite_superior)]
    print(f"Quantidade de outliers: {len(outliers)}")

    print("\n")
