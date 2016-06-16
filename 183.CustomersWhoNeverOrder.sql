select Name Customers 
from Customers left join 
(select distinct CustomerId ocid from Orders) t on id = ocid
where ocid is null
