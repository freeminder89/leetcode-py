select distinct num as num from 
(select id, num, if(@a = num, @b:=@b+1, @b:=1) cid,@a:=num
from Logs, (select @a:=null, @b:=0) val)t where cid > 2
