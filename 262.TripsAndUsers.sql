select Request_at Day, round(count(if(Status != 'completed', 1, null))/count(1), 2) "Cancellation Rate"
from 
Trips join Users on Client_Id = Users_Id and Banned = 'No'
where Request_at between '2013-10-01' and '2013-10-03'
group by Request_at
