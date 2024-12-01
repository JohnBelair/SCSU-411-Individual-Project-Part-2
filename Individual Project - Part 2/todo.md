# Database Design Description:

## Tables:

### Movies:
- `MovieID` (Primary Key): Unique identifier for each movie.
- `Title`: Title of the movie.
- `ReleaseYear`: The year the movie was released.
- `Rating`: The rating of the movie.
- `Description`: The description of the movie.
- `DirectorID`:(Foriegn Key): Unique identifier for each Director.

### Genres:
- `GenreID` (Primary Key): Unique identifier for each genre.
- `GenreName`: Name of the genre.

### Directors:
- `DirectorID` (Primary Key): Unique identifier for each director.
- `DirectorName`: Name of the director.
- `BirthDate`: The year the director was born.


### Actors:
- `ActorID` (Primary Key): Unique identifier for each actor.
- `ActorName`: Name of the actor.
- `BirthDate`: The year the actor was born.

### MovieGenres:
- `MovieID` (Foriegn Key): Unique identifier for each movie.
- `GenreID` (Foriegn Key): Unique identifier for each genre.

### MovieActors:
- `MovieID` (Foriegn Key): Unique identifier for each movie.
- `ActorID` (Foriegn Key): Unique identifier for each actor.


## Relationships:

- **Movies and Genres (Many-to-Many):**
  - Each movie can have multipe genres.
  - Each genre can be attributed to multiple movies.
  - This relationship is represented by an intermediary table, typically called `MovieGenres`, which stores pairs of `MovieID` and `GenreID`.

- **Movies and Actors (Many-to-Many):**
  - Each movie can have multipe actors.
  - Each actor can have stared to multiple movies.
  - This relationship is represented by an intermediary table, typically called `MovieActors`, which stores pairs of `MovieID` and `ActorID`.

- **Directors and Movies (One-to-Many):**
  - Each movie has one director.
  - Each director can have directed multiple movies.
  - The `DirectorID` in the `Movies` table serves as the foreign key.
---

## Create the Database:
- Open the terminal and enter the command 'cd db' to change the working directory to the db folder
- Create a new database: .\sqlite3 movies.db
- Create the tables using:.read database_script.sql
- Exit the SQlite part of the terminal by entering the .exit command

## Create the Database with Index:
- Open the terminal and enter the command 'cd db' to change the working directory to the db folder
- Create a new database: .\sqlite3 movies.db
- Create the tables using:.read database_with_index_script.sql
- Exit the SQlite part of the terminal by entering the .exit command

## Query the Database:
- Open the terminal and enter the command 'cd db' to change the working directory to the db folder
- Open the SQlite command line with the command .\sqlite3 movies.db
- Query the tables using:.read movie_count.sql
- Exit the SQlite part of the terminal by entering the .exit command
