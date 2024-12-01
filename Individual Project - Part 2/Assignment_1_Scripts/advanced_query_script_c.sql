-- Query C
SELECT m.MovieID, m.Title
FROM Movies m
LEFT JOIN MovieGenres mg ON m.MovieID = mg.MovieID
LEFT JOIN MovieActors ma ON m.MovieID = ma.MovieID
WHERE mg.MovieID IS NULL OR ma.MovieID IS NULL;