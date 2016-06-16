select e.name Employee 
from Employee e join Employee m
on e.ManagerId = m.id
where e.salary > m.salary
