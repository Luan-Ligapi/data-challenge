from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd

def create_connection(host, user, password, database=None, port=3306):
    """
    Cria uma conexão com o banco de dados MySQL usando SQLAlchemy.

    Parâmetros:
    - host (str): Endereço IP ou hostname do servidor MySQL.
    - user (str): Nome de usuário para autenticação no MySQL.
    - password (str): Senha para autenticação no MySQL.
    - database (str, opcional): Nome do banco de dados a ser utilizado. Padrão é None, ou seja, não define um banco específico.
    - port (int, opcional): Porta do MySQL. O padrão é 3306.

    Retorno:
    - engine: Objeto de conexão do SQLAlchemy.
    """
    try:
        # String de conexão do SQLAlchemy
        db_url = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database or ''}"
        engine = create_engine(db_url)
        print("Conexão ao MySQL estabelecida com sucesso!")
        return engine
    except SQLAlchemyError as err:
        print(f"Erro ao conectar ao MySQL: {err}")
        return None

def execute_query(engine, query):
    """
    Executa uma consulta SQL no banco de dados MySQL usando SQLAlchemy.

    Parâmetros:
    - engine: Objeto de conexão do SQLAlchemy.
    - query (str): A consulta SQL a ser executada.

    Retorno:
    - result: DataFrame contendo o resultado da consulta.
    """
    try:
        with engine.connect() as conn:
            result = pd.read_sql(text(query), conn)
            return result
    except SQLAlchemyError as err:
        print(f"Erro ao executar a consulta: {err}")
        return None

def close_connection(engine):
    """
    Fecha a conexão com o banco de dados MySQL usando SQLAlchemy.

    Parâmetros:
    - engine: Objeto de conexão do SQLAlchemy.
    """
    if engine:
        engine.dispose()
        print("Conexão ao MySQL foi encerrada.")

# Exemplo de uso:
if __name__ == "__main__":
    engine = create_connection("35.199.115.174", "looqbox-challenge", "looq-challenge", "looqbox-challenge")
    
    if engine:
        # Exemplo de consulta
        query = "SELECT * FROM data_product_sales LIMIT 10"
        resultado = execute_query(engine, query)
        if resultado is not None:
            print(resultado)
        
        # Fecha a conexão
        close_connection(engine)
