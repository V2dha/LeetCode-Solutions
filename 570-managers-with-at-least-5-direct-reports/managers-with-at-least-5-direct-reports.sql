# Write your MySQL query statement below
select b.name from 
(select a.id, a.name, count(*) as cnt 
from Employee a 
inner join Employee b 
on a.id = b.managerId
group by a.id, a.name) b
where cnt >= 5;
