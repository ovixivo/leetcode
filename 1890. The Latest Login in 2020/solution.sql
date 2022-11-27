/* Write your T-SQL query statement below */
SELECT a.user_id, a.time_stamp as last_stamp
FROM Logins a INNER JOIN
(
    SELECT user_id, max(time_stamp) as time_stamp
    FROM Logins
    WHERE YEAR(time_stamp) = 2020
    GROUP BY user_id
) b on a.user_id = b.user_id and a.time_stamp = b.time_stamp