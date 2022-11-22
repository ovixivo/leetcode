/* Write your T-SQL query statement below */
SELECT sell_date, count(distinct product) as num_sold,
STUFF(
    (SELECT distinct ',' + a.product
     FROM Activities a
     WHERE a.sell_date = b.sell_date
     FOR XML PATH('')), 1, 1, NULL) AS products
FROM Activities b
GROUP BY sell_date
ORDER BY sell_date