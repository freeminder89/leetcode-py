select s.score, sr.rank from Scores s join 
(select score,@rn := @rn + 1 as rank from
(select distinct score from Scores order by score desc) t, (select @rn:= 0 )r ) sr
on s.score = sr.score order by s.score desc;
