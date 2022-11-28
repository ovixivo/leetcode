/* Write your T-SQL query statement below */
SELECT u.user_id as buyer_id, u.join_date, CASE WHEN count(o.order_id) is NULL THEN 0 ELSE count(o.order_id) END as orders_in_2019
FROM Users u LEFT JOIN Orders o
    ON u.user_id = o.buyer_id and YEAR(o.order_date) = '2019'
GROUP BY u.user_id, u.join_date


