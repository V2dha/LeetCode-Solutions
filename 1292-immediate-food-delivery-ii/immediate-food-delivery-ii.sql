/* Write your PL/SQL query statement below */
-- with cte as 
-- (select customer_id, min(order_date) as first_order_date
-- from delivery
-- group by customer_id)
-- select 
-- round(sum(case 
-- when d.customer_pref_delivery_date=d.order_date 
-- then 1 else 0 end)*100/count(*),2) as immediate_percentage
-- from cte c
-- join delivery d
-- on c.customer_id = d.customer_id and c.first_order_date = d.order_date
-- ;

with cte as (
select  
rank() over (partition by customer_id order by order_date) as order_rnk,
case when customer_pref_delivery_date=order_date then 1 else 0 end order_int_count
from delivery
)
select round(sum(order_int_count)*100/count(*),2) as immediate_percentage from cte 
where order_rnk = 1;