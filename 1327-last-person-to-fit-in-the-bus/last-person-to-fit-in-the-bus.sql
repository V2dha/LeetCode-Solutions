/* Write your PL/SQL query statement below */
select q.person_name from 
( select 
person_name,
sum(weight) over (order by turn) as final_wt
from queue
order by sum(weight) over (order by turn) desc
) q
where q.final_wt <= 1000
and rownum = 1;

