select e.name as employee from employee e
inner join employee m
on e.managerId = m.id 
where e.salary > m.salary;