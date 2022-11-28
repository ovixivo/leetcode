/* Write your T-SQL query statement below */
SELECT u.name, CASE WHEN sum(r.distance) is NULL THEN 0 ELSE sum(r.distance) END as travelled_distance
FROM Users u LEFT JOIN Rides r
    ON u.id = r.user_id
GROUP BY r.user_id, u.name
ORDER BY sum(r.distance) desc, u.name