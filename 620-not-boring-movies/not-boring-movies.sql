# Write your MySQL query statement below

select a.id, a.movie, a.description, a.rating
from Cinema a
where a.id mod 2 != 0 
and description != 'boring'
order by rating desc