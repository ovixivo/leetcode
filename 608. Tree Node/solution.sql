/* Write your T-SQL query statement below */

SELECT id,
CASE 
    WHEN p_id is null THEN 'Root'
    WHEN exists (SELECT id FROM Tree t2 WHERE t1.id = t2.p_id) THEN 'Inner'
    ELSE 'Leaf' END
  AS type  

FROM Tree t1
ORDER BY id