select d.name Department, e.name Employee, e.salary Salary 
from 
(select DepartmentId did, max(salary) ms from Employee group by DepartmentId)t
join Employee e on t.did = e.DepartmentId and t.ms = e.salary
join Department d on t.did = d.id
