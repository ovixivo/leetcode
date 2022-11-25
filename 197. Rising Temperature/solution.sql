/* Write your T-SQL query statement below */
SELECT a.id
FROM Weather a, Weather b
WHERE a.recordDate = dateadd(day, 1, b.recordDate) 
    and a.temperature > b.temperature