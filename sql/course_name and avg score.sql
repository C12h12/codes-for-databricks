select c.course_name,avg(sub.score) as avg_score
from Courses c
join Assignments a on a.course_id=c.course_id
join Submissions sub on sub.assignment_id=a.assignment_id
group by c.course_name
order by avg(sub.score) desc;
