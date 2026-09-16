SELECT 
    dept.department_name,
    d.doctor_name,
    SUM(b.amount) AS total_revenue,
    RANK() OVER (
        PARTITION BY dept.department_name
        ORDER BY SUM(b.amount) DESC
    ) AS revenue_rank
FROM Departments dept
JOIN Doctors d 
    ON d.dept_id = dept.dept_id
JOIN Appointments a 
    ON a.doctor_id = d.doctor_id
JOIN Bills b 
    ON b.appointment_id = a.appointment_id
GROUP BY 
    dept.department_name,
    d.doctor_name;
