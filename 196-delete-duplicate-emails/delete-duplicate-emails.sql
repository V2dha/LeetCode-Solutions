delete from person
where id not in 
(select min(id) as id from person
group by email);