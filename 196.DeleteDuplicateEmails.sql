delete from 
Person where `id` not in (
select mid from 
(select Email, min(id) mid
from Person group by Email)t );
