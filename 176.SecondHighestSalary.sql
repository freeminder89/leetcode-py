select if(count(Salary)<2,null,min(Salary)) SecondHighestSalary from 
( select Salary from Employee group by Salary order by Salary desc limit 2) t
