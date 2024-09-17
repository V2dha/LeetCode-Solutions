/* Write your PL/SQL query statement below */
 with cte as (
 SELECT 
    id,
    num,
    id - DENSE_RANK() OVER (PARTITION BY num ORDER BY id) AS rn
  FROM logs ) 
  select distinct num as ConsecutiveNums from cte
  group by num, rn
  having count(rn) >= 3;