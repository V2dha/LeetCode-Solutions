/* Write your PL/SQL query statement below */
select id, num from 
(select id, count(*) as num from
(select requester_id as id from requestaccepted
union all
select accepter_id as id from requestaccepted)
group by id
order by count(*) desc)
where rownum =1;
