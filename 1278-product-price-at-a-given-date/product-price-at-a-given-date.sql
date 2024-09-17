with cte as (select distinct product_id from products)
select c.product_id, coalesce(a.new_price, 10) as price
from cte c
left join (
select product_id, new_price from
(select p.*,
max(change_date) over(partition by product_id) as max_date
from products p
where change_date <= '2019-08-16')
where change_date = max_date) a
on c.product_id = a.product_id;