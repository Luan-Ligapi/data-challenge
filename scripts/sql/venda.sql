SELECT p.PRODUCT_NAME, s.STORE_NAME, ps.SALES_VALUE, ps.SALES_QTY
FROM data_product_sales ps
JOIN data_product p ON ps.PRODUCT_CODE = p.PRODUCT_COD
JOIN data_store_cad s ON ps.STORE_CODE = s.STORE_CODE
WHERE p.PRODUCT_NAME = 'Produto Exemplo';
