/* Write your PL/SQL query statement below */

with cte as
(select count(*) as total_prd from product)
select customer_id
from customer 
group by customer_id
having count(distinct product_key) =
(select total_prd from cte)