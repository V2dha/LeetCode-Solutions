/* Write your PL/SQL query statement below */
with cte as 
(select reports_to, count(employee_id) as reports_count, 
round(sum(age)/count(employee_id)) as average_age 
from employees
where reports_to is not null
group by reports_to) 
select a.employee_id, a.name, c.reports_count, c.average_age from 
cte c inner join employees a
on c.reports_to = a.employee_id
order by a.employee_id
;