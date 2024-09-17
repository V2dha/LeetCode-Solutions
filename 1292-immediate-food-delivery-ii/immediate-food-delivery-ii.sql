/* Write your PL/SQL query statement below */
with cte as 
(select customer_id, min(order_date) as first_order_date
from delivery
group by customer_id)
select 
round(sum(case 
when d.customer_pref_delivery_date=d.order_date 
then 1 else 0 end)*100/count(*),2) as immediate_percentage
from cte c
join delivery d
on c.customer_id = d.customer_id and c.first_order_date = d.order_date
;
