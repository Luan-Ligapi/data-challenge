# Desafio de Dados Looqbox - Visão Geral da Solução

## Visão Geral do Desafio

A tarefa era analisar e manipular dados do banco de dados do desafio Looqbox. O desafio foi dividido em várias partes, onde respondemos a várias perguntas usando consultas SQL e scripts Python. As soluções envolveram consultar o banco de dados, calcular métricas-chave e visualizar os dados.

### As Três Tarefas Principais:

1. **Consultas SQL**:
- Recuperar os 10 produtos mais caros da empresa.
- Identificar as seções nos departamentos 'BEBIDAS' e 'PADARIA'.
- Calcular as vendas totais para cada área de negócios no primeiro trimestre de 2019.

2. **Função Python para consultar dados dinamicamente**:
Desenvolvemos uma função Python, `retrieve_data`, que consulta dinamicamente o banco de dados com base em três parâmetros de entrada:
- Código do produto (inteiro)
- Código da loja (inteiro)
- Intervalo de datas (lista de strings semelhantes a ISO)

3. **Ticket Médio**:
Usando a duas querys bases e um tratamento de dados cheguei ao retorno esperado

4. **Visualização de dados**:
Usando a tabela IMDB_movies, criei um gráfico de dispersão que ilustra a relação entre a classificação de um filme e o número de votos que ele recebeu.

---
## Análise da solução

### 1. Consultas SQL

#### Consulta 1: 10 produtos mais caros
```sql
SELECT PRODUCT_NAME, PRODUCT_VAL
FROM data_product
ORDER BY PRODUCT_VAL DESC
LIMIT 1;
```
Esta consulta retorna o produto com o maior valor (`PRODUCT_VAL`).

#### Consulta 2: Seções nos departamentos 'BEBIDAS' e 'PADARIA'
```sql
SELECT DISTINCT SECTION_NAME
FROM data_product
WHERE DEP_NAME IN ('BEBIDAS', 'PADARIA');
```
Esta consulta recupera todas as seções distintas nos departamentos 'BEBIDAS' e 'PADARIA'.

#### Consulta 3: Vendas totais no primeiro trimestre de 2019
```sql
SELECT BUSINESS_NAME, SUM(SALES_VALUE) AS total_sales
FROM data_store_sales
JOIN data_store_cad USING (STORE_CODE)
WHERE DATE BETWEEN '2019-01-01' AND '2019-03-31'
GROUP BY BUSINESS_NAME;
```
Esta consulta calcula as vendas totais para cada área de negócios no primeiro trimestre de 2019.

### 2. Função Python: `retrieve_data`

Esta função foi projetada para fazer consultas flexíveis ao banco de dados usando três parâmetros: código do produto, código da loja e um intervalo de datas. Abaixo está a implementação completa:

```python
def retrieve_data(product_code, store_code, date_range):
"""
Recupera dados de vendas com base no product_code, store_code e date_range fornecidos.
"""
engine = create_engine(DATABASE_URI)

query = f"""
SELECT STORE_CODE, PRODUCT_CODE, DATE, SALES_VALUE, SALES_QTY
FROM data_product_sales
WHERE PRODUCT_CODE = {product_code}
AND STORE_CODE = {store_code}
AND DATE BETWEEN '{date_range[0]}' E '{date_range[1]}';
"""

com engine.connect() como conexão:
df = pd.read_sql(query, connection)

return df
```


### 3. Ticket Médio
Gerei um código em python que trata o retorno dado pelo banco de dados

```python
    with engine.connect() as connection:
        df_store_cad = pd.read_sql(query1, connection)
        df_store_sales = pd.read_sql(query2, connection)

    # Converte a coluna 'DATE' para o formato datetime
    df_store_sales['DATE'] = pd.to_datetime(df_store_sales['DATE'])

    # Filtra as vendas entre '2019-10-01' e '2019-12-31'
    df_store_sales_filtered = df_store_sales[
        (df_store_sales['DATE'] >= '2019-10-01') &
        (df_store_sales['DATE'] <= '2019-12-31')
    ].copy()  # Aqui usamos .copy() para criar uma cópia explícita

    # Calcula o Ticket Médio (SALES_VALUE / SALES_QTY) por loja, usando .loc[] para evitar o alerta
    df_store_sales_filtered.loc[:, 'TM'] = df_store_sales_filtered['SALES_VALUE'] / df_store_sales_filtered['SALES_QTY']

    # Arredonda o Ticket Médio (TM) para 2 casas decimais
    df_store_sales_filtered['TM'] = df_store_sales_filtered['TM'].round(2)

    # Agrupa os dados por STORE_CODE e calcula a média do TM por loja
    df_ticket_medio = df_store_sales_filtered.groupby('STORE_CODE').agg({'TM': 'mean'}).reset_index()

    # Junta os dados de lojas com o Ticket Médio
    df_resultado = pd.merge(df_store_cad, df_ticket_medio, on='STORE_CODE', how='inner')

    # Seleciona as colunas desejadas e retorna o resultado final
    df_resultado_final = df_resultado[['STORE_NAME', 'BUSINESS_NAME', 'TM']]

    return df_resultado_final

```

### 4. Visualização: IMDB_movies

Gerei um gráfico de dispersão que mostra a relação entre o número de votos que um filme recebeu e sua classificação, com o ano de lançamento representado por cor.

```python
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
```

---

## Conclusão

Este desafio demonstrou o uso de SQL para consultar dados, Python para desenvolver funções dinâmicas para recuperar informações específicas e técnicas de visualização de dados para apresentar insights graficamente.