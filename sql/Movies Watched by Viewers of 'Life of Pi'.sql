SELECT 
    w.movie_id,
    m.title
FROM Watch_History w
JOIN Movies m 
    ON m.movie_id = w.movie_id
WHERE w.user_id IN (
    SELECT user_id
    FROM Watch_History
    WHERE movie_id = 902
)
GROUP BY 
    w.movie_id,
    m.title;
