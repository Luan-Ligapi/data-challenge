import unittest
from sqlalchemy import create_engine
import pandas as pd
import sys
import os

# Adiciona o caminho da pasta 'scripts' ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from scripts.caso2.consulta import calcular_ticket_medio

class TestCalcularTicketMedio(unittest.TestCase):

    def test_ticket_medio_format(self):
        """
        Testa se o DataFrame retornado pela função calcular_ticket_medio possui o formato correto,
        ou seja, as colunas 'STORE_NAME', 'BUSINESS_NAME' e 'TM'.
        """
        resultado = calcular_ticket_medio()

        # Verifica se o resultado é um DataFrame
        self.assertIsInstance(resultado, pd.DataFrame)

        # Verifica se as colunas corretas estão presentes
        colunas_esperadas = ['STORE_NAME', 'BUSINESS_NAME', 'TM']
        self.assertListEqual(list(resultado.columns), colunas_esperadas)

    def test_ticket_medio_valores(self):
        """
        Testa se os valores do Ticket Médio (TM) são numéricos e não negativos.
        """
        resultado = calcular_ticket_medio()

        # Verifica se os valores de TM são do tipo float e não são negativos
        self.assertTrue(all(isinstance(valor, float) for valor in resultado['TM']))
        self.assertTrue(all(valor >= 0 for valor in resultado['TM']))

if __name__ == "__main__":
    unittest.main()
