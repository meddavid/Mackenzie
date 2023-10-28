import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o DataFrame a partir de uma URL do github
url = "https://raw.githubusercontent.com/meddavid/Mackenzie-Projeto-Aplicado-I/adf5948da5b4b0f8fc2bee7fa4dad0ac60f23102/99.%20Artefatos/01.%20Dataset/vaccination-data.csv"
dados = pd.read_csv(url)

# Gráfico de barras para mostrar a quantidade de registros por WHO_REGION
plt.figure(figsize=(10, 6))  # Define o tamanho da figura
sns.countplot(data=dados, x='WHO_REGION')  # Cria um gráfico de barras usando Seaborn
plt.title('Quantidade de registros agrupados por WHO_REGION')  # Adiciona um título ao gráfico
plt.xlabel('Região da OMS')  # Rótulo do eixo X
plt.ylabel('Quantidade de Registros')  # Rótulo do eixo Y
plt.savefig('WHO_REGION_bar_plot.png', dpi=300)  # Salva o gráfico como .png com alta resolução
plt.close()  # Fecha a figura atual

# Lista das colunas numéricas que serão analisadas
colunas_numericas = [
    'TOTAL_VACCINATIONS_PER100',
    'PERSONS_VACCINATED_1PLUS_DOSE_PER100',
    'PERSONS_LAST_DOSE_PER100',
    'NUMBER_VACCINES_TYPES_USED'
]

# Loop para gerar histogramas e box plots para cada coluna numérica
for coluna in colunas_numericas:
    # Histograma
    plt.figure(figsize=(10, 6))
    sns.histplot(dados[coluna], bins=30, kde=True)  # Gera histograma com densidade KDE
    plt.title(f'Histograma da coluna {coluna}')  # Adiciona um título ao histograma
    plt.xlabel(coluna)  # Rótulo do eixo X
    plt.ylabel('Frequência')  # Rótulo do eixo Y
    plt.legend(labels=['Densidade KDE', 'Histograma'])  # Adiciona uma legenda
    plt.savefig(f'{coluna}_histogram.png', dpi=300)  # Salva o histograma como .png
    plt.close()  # Fecha a figura atual

    # Boxplot
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=dados[coluna])  # Gera box plot usando Seaborn
    plt.title(f'Box plot da coluna {coluna}')  # Adiciona um título ao box plot
    plt.xlabel(coluna)  # Rótulo do eixo X
    plt.ylabel('Valores')  # Rótulo do eixo Y
    plt.savefig(f'{coluna}_boxplot.png', dpi=300)  # Salva o box plot como .png
    plt.close()  # Fecha a figura atual
