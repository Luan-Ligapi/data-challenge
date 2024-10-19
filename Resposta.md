Quais são os 10 produtos mais caros da empresa?

Essa consulta irá buscar o produto com maior valor (product_val):

sql
Copiar código
SELECT PRODUCT_NAME, PRODUCT_VAL
FROM data_product
ORDER BY PRODUCT_VAL DESC
LIMIT 1;
