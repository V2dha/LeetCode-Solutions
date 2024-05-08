# Write your MySQL query statement below

select a.product_id, 
round(sum(a.total_price)/sum(a.units),2)
as average_price from
(select p.product_id, p.price*u.units as total_price, u.units
from Prices p
left join UnitsSold u 
on p.product_id = u.product_id 
where u.purchase_date between p.start_date and
p.end_date) a
group by a.product_id
union
select product_id, 0 as average_price
from Prices
where product_id not in 
(select product_id from UnitsSold)

