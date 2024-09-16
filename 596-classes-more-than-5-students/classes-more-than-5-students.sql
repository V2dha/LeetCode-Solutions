/* Write your PL/SQL query statement below */

select class from
(select class, count(distinct student) as cnt 
from Courses
group by class
)
where cnt >= 5;
