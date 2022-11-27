/* Write your T-SQL query statement below */
SELECT a.player_id, a.event_date as first_login
FROM Activity a INNER JOIN
(
SELECT player_id, min(event_date) as event_date
FROM Activity b
GROUP BY player_id
) c ON a.player_id = c.player_id and a.event_date = c.event_date
