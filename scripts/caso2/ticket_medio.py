from sqlalchemy import create_engine
import pandas as pd

# Configurações de conexão com SQLAlchemy
DATABASE_URI = "mysql+mysqlconnector://looqbox-challenge:looq-challenge@35.199.115.174:3306/looqbox-challenge"

def calcular_ticket_medio():
    """
    Função para calcular o Ticket Médio (TM) de vendas por loja durante o período de
    '2019-10-01' a '2019-12-31'. O Ticket Médio é calculado dividindo o valor total
    de vendas (SALES_VALUE) pela quantidade de vendas (SALES_QTY), retornando com duas
    casas decimais.

    A função realiza as seguintes operações:
    1. Consulta os dados das lojas (STORE_CODE, STORE_NAME, BUSINESS_NAME).
    2. Consulta os dados de vendas filtrados entre '2019-01-01' e '2019-12-31'.
    3. Filtra as vendas do período de '2019-10-01' a '2019-12-31'.
    4. Calcula o Ticket Médio (SALES_VALUE / SALES_QTY) por loja com duas casas decimais.
    5. Junta as informações de lojas com o Ticket Médio.

    Retorna:
        pandas.DataFrame: DataFrame com as colunas 'STORE_NAME', 'BUSINESS_NAME' e 'TM'
                          (Ticket Médio calculado para cada loja com duas casas decimais).
    """
    
    # Cria o engine do SQLAlchemy para conectar ao banco de dados
    engine = create_engine(DATABASE_URI)

    # Consulta 1: Informações das lojas
    query1 = """
    SELECT
        STORE_CODE,
        STORE_NAME,
        START_DATE,
        END_DATE,
        BUSINESS_NAME,
        BUSINESS_CODE
    FROM data_store_cad
    """

    # Consulta 2: Vendas no período de 2019-01-01 até 2019-12-31
    query2 = """
    SELECT
        STORE_CODE,
        DATE,
        SALES_VALUE,
        SALES_QTY
    FROM data_store_sales
    WHERE DATE BETWEEN '2019-01-01' AND '2019-12-31'
    """

    # Conectando e executando as consultas
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


# Exemplo de uso:
if __name__ == "__main__":
    resultado = calcular_ticket_medio()
    print(resultado)
