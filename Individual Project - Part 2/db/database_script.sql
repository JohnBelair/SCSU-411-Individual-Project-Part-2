-- Create Movies table with a foreign key to Directors
CREATE TABLE IF NOT EXISTS Movies (
    MovieID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT NOT NULL,
    ReleaseYear INTEGER,
    Rating REAL,
    Description TEXT,
    DirectorID INTEGER,
    FOREIGN KEY (DirectorID) REFERENCES Directors(DirectorID)
);

-- Create Genres table
CREATE TABLE IF NOT EXISTS Genres (
    GenreID INTEGER PRIMARY KEY AUTOINCREMENT,
    GenreName TEXT NOT NULL
);

-- Create Directors table
CREATE TABLE IF NOT EXISTS Directors (
    DirectorID INTEGER PRIMARY KEY AUTOINCREMENT,
    DirectorName TEXT NOT NULL,
    BirthDate DATE
);

-- Create Actors table
CREATE TABLE IF NOT EXISTS Actors (
    ActorID INTEGER PRIMARY KEY AUTOINCREMENT,
    ActorName TEXT NOT NULL,
    BirthDate DATE
);

-- Create MovieGenres table to represent many-to-many relationship between Movies and Genres
CREATE TABLE IF NOT EXISTS MovieGenres (
    MovieID INTEGER,
    GenreID INTEGER,
    FOREIGN KEY (MovieID) REFERENCES Movies(MovieID),
    FOREIGN KEY (GenreID) REFERENCES Genres(GenreID),
    PRIMARY KEY (MovieID, GenreID)
);

-- Create MovieActors table to represent many-to-many relationship between Movies and Actors
CREATE TABLE IF NOT EXISTS MovieActors (
    MovieID INTEGER,
    ActorID INTEGER,
    FOREIGN KEY (MovieID) REFERENCES Movies(MovieID),
    FOREIGN KEY (ActorID) REFERENCES Actors(ActorID),
    PRIMARY KEY (MovieID, ActorID)
);