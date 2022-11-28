/* Write your T-SQL query statement below */

SELECT buy.stock_name, (sell_price - buy_price) as capital_gain_loss
FROM
(
    SELECT stock_name, sum(price) as buy_price
    FROM Stocks
    GROUP BY stock_name, operation
    HAVING operation = 'Buy'
) buy
    INNER JOIN
(
    SELECT stock_name, sum(price) as sell_price
    FROM Stocks
    GROUP BY stock_name, operation
    HAVING operation = 'Sell'
) sell
ON buy.stock_name = sell.stock_name