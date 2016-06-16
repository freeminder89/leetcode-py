select d.name Department, er.name Employee , er.salary Salary  from 
Department d join 
(select 
t.*, 
case when @did = t.DepartmentId then if(@presal = salary or (@presal := salary) is null, @rank, @rank := @rank + 1) 
     when (@did := t.DepartmentId) is not null and (@presal := salary) is not null then @rank := 1
     end rank
from 
(select *
from Employee  
order by DepartmentId, salary desc) t, (select @did:=null,@rank:=1, @presal:=0) val ) er
on d.id = er.DepartmentId
where er.rank <= 3
order by er.DepartmentId asc, er.salary desc
