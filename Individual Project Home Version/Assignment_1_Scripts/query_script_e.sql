--Query E:
SELECT g.GenreName, AVG(m.Rating) AS AverageRating
FROM Genres g
JOIN MovieGenres mg ON g.GenreID = mg.GenreID
JOIN Movies m ON mg.MovieID = m.MovieID
GROUP BY g.GenreID, g.GenreName;