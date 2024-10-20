import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Configurações da conexão com SQLAlchemy
DATABASE_URI = "mysql+mysqlconnector://looqbox-challenge:looq-challenge@35.199.115.174:3306/looqbox-challenge"

def visualizar_imdb_movies():
    """
    Função que gera um gráfico de dispersão (scatter plot) para a tabela IMDB_movies,
    relacionando a avaliação dos filmes (rating) com a quantidade de votos (votes),
    e utilizando o ano de lançamento como uma variável de cor.

    A função realiza os seguintes passos:
    1. Consulta a tabela IMDB_movies.
    2. Gera um gráfico de dispersão usando 'rating' no eixo Y e 'votes' no eixo X.
    3. A cor dos pontos representa o ano de lançamento dos filmes.
    4. Exibe o gráfico.
    """

    # Cria o engine para conectar ao banco de dados
    engine = create_engine(DATABASE_URI)

    # Consulta a tabela IMDB_movies
    query = """
    SELECT
        title,
        rating,
        votes,
        year
    FROM IMDB_movies
    """
    
    # Conectando e carregando os dados em um DataFrame
    with engine.connect() as connection:
        df_imdb = pd.read_sql(query, connection)

    # Configurando o estilo do gráfico
    plt.figure(figsize=(10, 6))
    sns.set(style="whitegrid")

    # Criando o gráfico de dispersão (scatter plot)
    scatter = sns.scatterplot(
        x='votes', 
        y='rating', 
        hue='year', 
        palette='viridis', 
        data=df_imdb, 
        size='votes', 
        sizes=(40, 400), 
        alpha=0.7, 
        edgecolor=None
    )

    # Adicionando títulos e rótulos
    scatter.set_title("Relação entre Avaliação (Rating) e Votos (Votes) dos Filmes")
    scatter.set_xlabel("Quantidade de Votos")
    scatter.set_ylabel("Avaliação Média (Rating)")

    # Exibindo o gráfico
    plt.show()

# Exemplo de execução
if __name__ == "__main__":
    visualizar_imdb_movies()
