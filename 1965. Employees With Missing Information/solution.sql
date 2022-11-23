/* Write your T-SQL query statement below */
SELECT (CASE 
            WHEN e.employee_id IS null 
            THEN s.employee_id 
            ELSE e.employee_id 
        END) AS employee_id 
FROM Employees e FULL OUTER JOIN  Salaries s
        on e.employee_id = s.employee_id
WHERE e.name is null or s.salary is null
ORDER BY employee_id