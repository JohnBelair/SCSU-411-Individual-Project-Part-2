-- Query B:
SELECT m.Title, m.ReleaseYear
FROM Movies m
WHERE m.ReleaseYear > 2010
ORDER BY m.ReleaseYear DESC;