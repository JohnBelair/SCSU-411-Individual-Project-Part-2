-- Insert genres
INSERT INTO Genres (GenreName) VALUES 
('Action'),
('Drama'),
('Comedy'),
('Sci-Fi'),
('Thriller');

-- Insert directors
INSERT INTO Directors (DirectorName, BirthDate) VALUES 
('Steven Spielberg', '1946-12-18'),
('Christopher Nolan', '1970-07-30'),
('Quentin Tarantino', '1963-03-27'),
('Martin Scorsese', '1942-11-17'),
('Greta Gerwig', '1983-08-04'),
('Kathryn Bigelow', '1951-11-27'),
('Denis Villeneuve', '1967-10-03');

-- Insert actors
INSERT INTO Actors (ActorName, BirthDate) VALUES 
('Leonardo DiCaprio', '1974-11-11'),
('Robert Downey Jr.', '1965-04-04'),
('Scarlett Johansson', '1984-11-22'),
('Tom Hanks', '1956-07-09'),
('Emma Stone', '1988-11-06'),
('Ryan Gosling', '1980-11-12'),
('Jennifer Lawrence', '1990-08-15'),
('Brad Pitt', '1963-12-18'),
('Natalie Portman', '1981-06-09'),
('Christian Bale', '1974-01-30'),
('Anne Hathaway', '1982-11-12'),
('Joaquin Phoenix', '1974-10-28'),
('Daniel Craig', '1968-03-02'),
('Chris Evans', '1981-06-13'),
('Meryl Streep', '1949-06-22');

-- Insert movies and associate with directors
INSERT INTO Movies (Title, ReleaseYear, Rating, Description, DirectorID) VALUES 
('Inception', 2010, 8.8, 'A mind-bending thriller', 2),
('The Dark Knight', 2008, 9.0, 'Batman faces the Joker', 2),
('Interstellar', 2014, 8.6, 'A journey through space and time', 2),
('Pulp Fiction', 1994, 8.9, 'Interwoven stories of crime', 3),
('Dunkirk', 2017, 7.9, 'World War II evacuation', 2),
('Catch Me If You Can', 2002, 8.1, 'A true story of a con artist', 1),
('The Irishman', 2019, 7.9, 'An aging hitman recalls his past', 4),
('Lady Bird', 2017, 7.4, 'A teenager explores life', 5),
('Arrival', 2016, 7.9, 'Alien contact with linguistics', 7),
('Zero Dark Thirty', 2012, 7.4, 'Hunt for Osama bin Laden', 6),
('Unassigned Movie 1', 2020, 6.5, 'A mystery movie without genre or actors', 3), -- No genre or actors
('Unassigned Movie 2', 2021, 7.2, 'Another movie missing genre and actors', 4); -- No genre or actors

-- Insert into MovieGenres to associate movies with genres
INSERT INTO MovieGenres (MovieID, GenreID) VALUES 
(1, 4), (1, 5),  -- Inception: Sci-Fi, Thriller
(2, 1), (2, 5),  -- The Dark Knight: Action, Thriller
(3, 4),          -- Interstellar: Sci-Fi
(4, 3),          -- Pulp Fiction: Comedy
(5, 1),          -- Dunkirk: Action
(6, 2),          -- Catch Me If You Can: Drama
(7, 2),          -- The Irishman: Drama
(8, 2),          -- Lady Bird: Drama
(9, 4),          -- Arrival: Sci-Fi
(10, 1), (10, 2); -- Zero Dark Thirty: Action, Drama

-- Insert into MovieActors to associate movies with actors
INSERT INTO MovieActors (MovieID, ActorID) VALUES 
(1, 1), (1, 3), (1, 5),         -- Inception: Leonardo DiCaprio, Scarlett Johansson, Emma Stone
(2, 1), (2, 10), (2, 14),       -- The Dark Knight: Leonardo DiCaprio, Christian Bale, Chris Evans
(3, 3), (3, 4), (3, 6),         -- Interstellar: Scarlett Johansson, Tom Hanks, Ryan Gosling
(4, 2), (4, 8), (4, 12),        -- Pulp Fiction: Robert Downey Jr., Brad Pitt, Joaquin Phoenix
(5, 10), (5, 14),               -- Dunkirk: Christian Bale, Chris Evans
(6, 4), (6, 9),                 -- Catch Me If You Can: Tom Hanks, Natalie Portman
(7, 11), (7, 15),               -- The Irishman: Anne Hathaway, Meryl Streep
(8, 5), (8, 7),                 -- Lady Bird: Emma Stone, Jennifer Lawrence
(9, 9), (9, 13),                -- Arrival: Natalie Portman, Daniel Craig
(10, 10), (10, 14), (10, 8);    -- Zero Dark Thirty: Christian Bale, Chris Evans, Brad Pitt