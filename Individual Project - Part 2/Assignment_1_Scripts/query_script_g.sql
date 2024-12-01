--Query G:
SELECT m.Title, COUNT(ma.ActorID) AS ActorCount
FROM Movies m
JOIN MovieActors ma ON m.MovieID = ma.MovieID
GROUP BY m.MovieID, m.Title
HAVING COUNT(ma.ActorID) >= 3;