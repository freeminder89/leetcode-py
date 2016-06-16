CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select if(count(Salary)<N,null,min(Salary)) SecondHighestSalary from 
( select Salary from Employee group by Salary order by Salary desc limit N) t
      
  );
END
