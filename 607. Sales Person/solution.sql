/* Write your T-SQL query statement below */
SELECT s.name
FROM Orders o INNER JOIN 
    (SELECT com_id FROM Company WHERE name = 'RED') c
    ON o.com_id = c.com_id RIGHT JOIN SalesPerson s
    ON o.sales_id = s.sales_id
WHERE o.order_id is NULL