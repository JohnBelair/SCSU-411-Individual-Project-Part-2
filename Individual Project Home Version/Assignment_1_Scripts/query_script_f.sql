--Query F:
SELECT DISTINCT a.ActorName
FROM Actors a
JOIN MovieActors ma ON a.ActorID = ma.ActorID
JOIN Movies m ON ma.MovieID = m.MovieID
JOIN MovieGenres mg ON m.MovieID = mg.MovieID
JOIN Genres g ON mg.GenreID = g.GenreID
WHERE g.GenreName = 'Action';