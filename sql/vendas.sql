SELECT s.STORE_NAME, SUM(ps.SALES_VALUE) AS total_sales
FROM data_product_sales ps
JOIN data_store_cad s ON ps.STORE_CODE = s.STORE_CODE
GROUP BY s.STORE_NAME;
