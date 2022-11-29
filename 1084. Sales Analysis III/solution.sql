/* Write your T-SQL query statement below */
SELECT p.product_id, p.product_name
FROM Product p
WHERE NOT EXISTS(
    SELECT s.product_id
    FROM Sales s
    WHERE p.product_id = s.product_id AND
            sale_date not between '2019-01-01' and '2019-03-31'
) AND 
EXISTS(
    SELECT s.product_id
    FROM Sales s
    WHERE p.product_id = s.product_id AND
            sale_date between '2019-01-01' and '2019-03-31'
)