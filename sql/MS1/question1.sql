select e.event_name,a.athlete_name,r.finish_time,
round(avg(r.finish_time) over(partition by e.event_name) , 2)as avg_event_time
from Results r
join Events e on r.event_id=e.event_id
join Athletes a on a.athlete_id=r.athlete_id
where r.status='Recorded'
order by e.event_name,r.finish_time,a.athlete_name;
