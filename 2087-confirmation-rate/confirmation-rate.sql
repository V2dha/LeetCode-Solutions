# Write your MySQL query statement below
select c.user_id, 
coalesce(round(b.confirmed/a.total, 2), 0) as 
confirmation_rate from Signups c
left join
(select user_id, count(*) as total
from Confirmations
group by user_id) a
on a.user_id = c.user_id
left join 
(select user_id, count(*) as confirmed
from Confirmations
where action = 'confirmed'
group by user_id) b
on a.user_id = b.user_id
-- union
-- select user_id, 0 as confirmation_rate from
-- Signups where user_id not in 
-- (select user_id from Confirmations)

