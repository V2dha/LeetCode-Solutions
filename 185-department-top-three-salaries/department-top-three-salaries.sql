/* Write your PL/SQL query statement below */
with cte as 
(select id, name, salary, departmentId,
dense_rank() over (partition by departmentId order by salary desc) as rnk
from employee)
select d.name as Department,
e.name as employee,
e.salary
from cte e
left join department d
on d.id = e.departmentId
where rnk < 4;