--Query C:
SELECT m.Title, m.Rating, d.DirectorName
FROM Movies m
JOIN Directors d ON m.DirectorID = d.DirectorID
ORDER BY m.Rating DESC
LIMIT 5;