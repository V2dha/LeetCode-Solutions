/* Write your PL/SQL query statement below */

--round(sum(tiv_2016),2) where same tiv_2015 as one or more other pid
-- and do not have same lat and lon

select round(sum(tiv_2016),2) as tiv_2016 from insurance
where tiv_2015 in (select tiv_2015 from insurance
group by tiv_2015 having count(*) > 1)
and concat(lat, lon) not in (select concat(lat, lon) from
insurance group by lat, lon having count(*) > 1);
