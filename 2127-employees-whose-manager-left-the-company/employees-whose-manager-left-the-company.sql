SELECT employee_id
FROM Employees e
WHERE NOT EXISTS (
    SELECT 1
    FROM Employees m
    WHERE e.manager_id = m.employee_id
)
AND salary < 30000
and e.manager_id is not null
ORDER BY employee_id;

