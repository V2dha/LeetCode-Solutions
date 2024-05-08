# Write your MySQL query statement below
with cte as
(select count(user_id) as total from Users)
select r.contest_id,
round((count(u.user_id)/(select total from cte))*100, 2) as percentage
from Register r
join Users u
on u.user_id = r.user_id 
group by r.contest_id
order by percentage desc, r.contest_id asc