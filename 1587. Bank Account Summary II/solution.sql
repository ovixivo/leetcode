/* Write your T-SQL query statement below */
SELECT u.name, SUM(amount) as balance
FROM Users u INNER JOIN Transactions t
    ON u.account = t.account
GROUP BY u.name
HAVING SUM(amount) > 10000