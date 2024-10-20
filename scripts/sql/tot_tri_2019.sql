SELECT sc.BUSINESS_NAME, SUM(ps.SALES_VALUE) AS total_sales
FROM data_product_sales ps
JOIN data_store_cad sc ON ps.STORE_CODE = sc.STORE_CODE
WHERE ps.DATE BETWEEN '2019-01-01' AND '2019-03-31'
GROUP BY sc.BUSINESS_NAME;


--Essa consulta irá calcular a venda total por área de negócios, filtrando as vendas do primeiro trimestre de 2019

