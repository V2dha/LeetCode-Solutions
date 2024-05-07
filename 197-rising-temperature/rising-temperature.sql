# Write your MySQL query statement below
select w1.id from weather w1
left join 
(select temperature, date_add(recordDate, interval 1 day)
as recordDate from weather) w2
on w1.recordDate = w2.recordDate
where w1.temperature > w2.temperature

