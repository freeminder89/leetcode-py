select w1.Id Id
from Weather w1 join Weather w2 on datediff(w1.Date, w2.Date) = 1
where w1.Temperature > w2.Temperature;
