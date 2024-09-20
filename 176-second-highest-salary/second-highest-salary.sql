/* Write your PL/SQL query statement below */
with cte as
(
    select id, 
    salary,
    dense_rank() over (order by salary desc) as rnk
    from employee
)
select 
max(case when rnk = 2 then salary else null end) as SecondHighestSalary
from cte;