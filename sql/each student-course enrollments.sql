select s.student_id,s.name as student_name,e.course_id,c.course_name,e.grade,d.department_name
from Students s
join Enrollments e on s.student_id=e.student_id
join Courses c on e.course_id=c.course_id
join Departments d on c.department_id=d.department_id
order by s.name;
