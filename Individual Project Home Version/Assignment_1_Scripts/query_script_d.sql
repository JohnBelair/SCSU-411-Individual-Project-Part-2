--Query D:
SELECT d.DirectorName, COUNT(m.MovieID) AS MovieCount
FROM Directors d
JOIN Movies m ON d.DirectorID = m.DirectorID
GROUP BY d.DirectorID, d.DirectorName
HAVING COUNT(m.MovieID) >= 3;