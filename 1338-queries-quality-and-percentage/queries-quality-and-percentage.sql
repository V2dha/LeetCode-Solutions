# Write your MySQL query statement below

select a.query_name,
round(sum(a.rating/a.position)/count(*), 2) as quality,
coalesce(round((b.poor_total/count(*))*100,2),0)
as poor_query_percentage
from 
(select * from Queries where query_name is 
not null) a
left join 
(select query_name, count(*) as poor_total from Queries
where rating < 3 group by query_name) b
on a.query_name = b.query_name
group by a.query_name
