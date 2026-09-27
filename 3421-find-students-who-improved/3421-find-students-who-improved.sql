SELECT 
    student_id,
    subject,
    MAX(CASE WHEN exam_date = first_date THEN score END) AS first_score,
    MAX(CASE WHEN exam_date = latest_date THEN score END) AS latest_score
FROM (
    SELECT 
        student_id,
        subject,
        score,
        exam_date,
        MIN(exam_date) OVER (PARTITION BY student_id, subject) AS first_date,
        MAX(exam_date) OVER (PARTITION BY student_id, subject) AS latest_date
    FROM Scores
) t
GROUP BY student_id, subject
HAVING latest_score > first_score
ORDER BY student_id, subject;