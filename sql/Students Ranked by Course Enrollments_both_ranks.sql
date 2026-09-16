SELECT 
    s.student_id,
    s.name,
    COUNT(e.course_id) AS course_count,
    RANK() OVER (
        ORDER BY COUNT(e.course_id) DESC
    ) AS rank_by_enrollments,
    DENSE_RANK() OVER (
        ORDER BY COUNT(e.course_id) DESC
    ) AS dense_rank_by_enrollments
FROM Students s
JOIN Enrollments e 
    ON e.student_id = s.student_id
GROUP BY 
    s.student_id,
    s.name
ORDER BY rank_by_enrollments;
