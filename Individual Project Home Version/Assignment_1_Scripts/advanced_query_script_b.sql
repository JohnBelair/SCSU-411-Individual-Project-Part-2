-- Query B
SELECT d.DirectorName, m.Title AS HighestRatedMovie, m.Rating
FROM Directors d
JOIN Movies m ON d.DirectorID = m.DirectorID
WHERE m.Rating = (
    SELECT MAX(m2.Rating)
    FROM Movies m2
    WHERE m2.DirectorID = d.DirectorID
);