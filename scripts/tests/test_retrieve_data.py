import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.caso1.retrieve_data import retrieve_data
import pandas as pd


class TestRetrieveData(unittest.TestCase):

    def test_retrieve_data_with_valid_input(self):
        """
        Teste para verificar se a função retorna dados quando parâmetros válidos são passados.
        """
        product_code = 18
        store_code = 1
        date_range = ['2019-01-01', '2019-01-10']
        
        # Chama a função para obter os dados
        result = retrieve_data(product_code, store_code, date_range)
        
        # Verifica se o resultado não está vazio
        self.assertFalse(result.empty, "O DataFrame retornado não deveria estar vazio")
        
        # Verifica se o DataFrame contém as colunas esperadas
        expected_columns = ['STORE_CODE', 'PRODUCT_CODE', 'DATE', 'SALES_VALUE', 'SALES_QTY']
        self.assertListEqual(list(result.columns), expected_columns, "As colunas do DataFrame não são as esperadas")
        
        # Verifica se o DataFrame contém o número correto de linhas
        self.assertEqual(len(result), 10, "O número de linhas retornadas está incorreto")

    def test_retrieve_data_with_no_data(self):
        """
        Teste para verificar se a função lida corretamente com um caso onde não há dados.
        """
        product_code = 99999  # Valor que provavelmente não existe
        store_code = 1
        date_range = ['2019-01-01', '2019-01-10']
        
        # Chama a função para obter os dados
        result = retrieve_data(product_code, store_code, date_range)
        
        # Verifica se o resultado está vazio
        self.assertTrue(result.empty, "O DataFrame deveria estar vazio para um product_code inexistente")
    
    def test_retrieve_data_with_invalid_date_range(self):
        """
        Teste para verificar se a função lida corretamente com um intervalo de datas inválido.
        """
        product_code = 18
        store_code = 1
        date_range = ['2025-01-01', '2025-01-10']  # Data futura, que provavelmente não tem dados
        
        # Chama a função para obter os dados
        result = retrieve_data(product_code, store_code, date_range)
        
        # Verifica se o resultado está vazio
        self.assertTrue(result.empty, "O DataFrame deveria estar vazio para um intervalo de datas no futuro")
    
    def test_retrieve_data_with_invalid_product_code(self):
        """
        Teste para verificar se a função lida corretamente com um product_code inválido.
        """
        product_code = 'invalid'  # Código de produto inválido
        store_code = 1
        date_range = ['2019-01-01', '2019-01-10']
        
        # Tenta chamar a função, esperando que ela lance um erro
        with self.assertRaises(Exception):
            retrieve_data(product_code, store_code, date_range)

if __name__ == '__main__':
    unittest.main()
