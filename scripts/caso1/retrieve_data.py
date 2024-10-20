from sqlalchemy import create_engine
import pandas as pd

def retrieve_data(product_code, store_code, date_range):
    """
    Função para recuperar dados da tabela data_product_sales com base no código do produto,
    código da loja e intervalo de datas.

    Parâmetros:
    - product_code (int): Código do produto a ser filtrado.
    - store_code (int): Código da loja a ser filtrado.
    - date_range (list): Lista de duas strings representando a data inicial e final no formato ISO.
    
    Retorno:
    - pandas.DataFrame: DataFrame contendo os dados recuperados da consulta.
    """
    
    # Criar a conexão com SQLAlchemy usando o driver MySQL
    engine = create_engine('mysql+mysqlconnector://looqbox-challenge:looq-challenge@35.199.115.174:3306/looqbox-challenge')
    
    # Montando a consulta SQL dinâmica
    query = f"""
    SELECT *
    FROM data_product_sales
    WHERE PRODUCT_CODE = {product_code}
      AND STORE_CODE = {store_code}
      AND DATE BETWEEN '{date_range[0]}' AND '{date_range[1]}'
    """
    
    # Executando a consulta e convertendo os resultados para um DataFrame
    df = pd.read_sql(query, engine)
    
    return df

# Exemplo de uso:
my_data = retrieve_data(12345, 678, ['2019-01-01', '2019-01-31'])
print(my_data)
