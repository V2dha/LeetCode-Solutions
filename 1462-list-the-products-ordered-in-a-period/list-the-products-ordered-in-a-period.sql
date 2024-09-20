/* Write your PL/SQL query statement below */


select p.product_name,
o.unit as unit
from products p
join 
(select
    product_id, sum(unit) as unit
    from orders 
    where extract(year from order_date) = 2020
    and extract(month from order_date) = 2
    group by product_id
    having sum(unit) >= 100
) o
on o.product_id = p.product_id;

