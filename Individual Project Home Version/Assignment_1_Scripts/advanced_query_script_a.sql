-- Query A
SELECT a.ActorName, COUNT(DISTINCT g.GenreID) AS GenreCount
FROM Actors a
JOIN MovieActors ma ON a.ActorID = ma.ActorID
JOIN Movies m ON ma.MovieID = m.MovieID
JOIN MovieGenres mg ON m.MovieID = mg.MovieID
JOIN Genres g ON mg.GenreID = g.GenreID
GROUP BY a.ActorID, a.ActorName
ORDER BY GenreCount DESC
LIMIT 3;