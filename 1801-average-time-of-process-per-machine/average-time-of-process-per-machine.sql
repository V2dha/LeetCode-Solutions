# Write your MySQL query statement below

select a.machine_id, round(avg(a.process), 3) as processing_time from
(
select s.machine_id, e.timestamp - s.timestamp as process from
(select * from Activity where activity_type = 'start') s
join 
(select * from Activity where activity_type = 'end') e
on s.machine_id = e.machine_id
and s.process_id = e.process_id 
) a
group by a.machine_id

