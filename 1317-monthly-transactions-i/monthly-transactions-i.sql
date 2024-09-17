/* Write your PL/SQL query statement below */

with cte as (select to_char(trans_date, 'YYYY-MM') as month, country, 
count(id) as trans_count, sum(amount) as trans_total_amount
from transactions 
group by to_char(trans_date, 'YYYY-MM') , country)
select c.month, c.country, c.trans_count, coalesce(a.approved_count, 0) as approved_count, 
c.trans_total_amount, coalesce(a.approved_total_amount,0) as approved_total_amount from cte c
left join 
(select to_char(trans_date, 'YYYY-MM') as month, country, count(id) as approved_count,
sum(amount) as approved_total_amount
from transactions 
where state = 'approved'
group by to_char(trans_date, 'YYYY-MM'), country) a
on (a.month = c.month OR (a.month IS NULL AND c.month IS NULL))
AND (a.country = c.country OR (a.country IS NULL AND c.country IS NULL));