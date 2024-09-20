select to_char(sell_date, 'YYYY-MM-DD') as sell_date,
count(distinct product) as num_sold,
LISTAGG(product, ',') within group (order by product) as products
from (select distinct * from activities)
group by sell_date
order by sell_date;