#CSCI 411
#Database Theory and Design
#
#file: helper.py
# 
#Code snippets for the Individual Project - Part 2.
#Code included in snippet contained  "generate_genre", "generate_movie_title" and "generate_movie" methods.
#The "generate_actor" and "generate_director" methods were added after the fact.
#
# This program does all the generation for the database insertion functions
# The generate_genre(), generate_actor() and generate_director() methods all randomly
# choose a value from the predetermined list and return it to the app.py file.
# 
# The generate_movies() method takes in the variable "num_movies" which dictates
# how many movies the method creates and inserts into the database.
#
# The generate_movie_title() method is called by the generate_movies() method
# to generate movie titles for the method.


import random
import sqlite3
# Define the path to your SQLite database file
DATABASE = 'db/movies.db'

# randomly selects a genre from the list and returns it to the app.py file
def generate_genre():
    genres = ['Acton', 'Comedy', 'Drama', 'Fantasy', 'Horror', 'Mystery', 'Romance', 'Thriller', 'Sci-Fi', 'Western']
    return random.choice(genres)

# randomly selects a actor from the list and returns it to the app.py file
def generate_actor():
    actors = [('Leonardo DiCaprio', '1974-11-11'), ('Robert Downey Jr.', '1965-04-04'), ('Scarlett Johansson', '1984-11-22'), ('Tom Hanks', '1956-07-09'), ('Emma Stone', '1988-11-06'), 
              ('Ryan Gosling', '1980-11-12'), ('Jennifer Lawrence', '1990-08-15'), ('Brad Pitt', '1963-12-18'), ('Natalie Portman', '1981-06-09'), ('Christian Bale', '1974-01-30'), 
              ('Anne Hathaway', '1982-11-12'), ('Joaquin Phoenix', '1974-10-28'), ('Daniel Craig', '1968-03-02'), ('Chris Evans', '1981-06-13'), ('Meryl Streep', '1949-06-22')]
    return random.choice(actors)

# randomly selects a director from the list and returns it to the app.py file
def generate_director():
    directors = [('Steven Spielberg', '1946-12-18'), ('Christopher Nolan', '1970-07-30'), ('Quentin Tarantino', '1963-03-27'), 
                 ('Martin Scorsese', '1942-11-17'), ('Greta Gerwig', '1983-08-04'), ('Kathryn Bigelow', '1951-11-27'), 
                 ('Denis Villeneuve', '1967-10-03')]
    return random.choice(directors)

# randomly generates a movie title from the list and returns it to the generate_movies() method
def generate_movie_title():

    adjectives = [
    "Amazing", "Bewitched", "Charming", "Dazzling", "Enigmatic",
    "Fantastic", "Glorious", "Harmonious", "Incredible", "Jubilant",
    "Magical", "Radiant", "Spectacular", "Thrilling", "Wonderous"
    ]

    nouns = [
    "Adventure", "Dream", "Escape", "Fantasy", "Journey",
    "Mystery", "Odyssey", "Quest", "Voyage", "Legend",
    "Miracle", "Enchantment", "Whisper", "Wonder", "Treasure"
    ]

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    random_number = random.randint(1000, 9999)
    return f"{adjective} {noun} {random_number}"


# randomly generates a movie from the attributes and adds to the database
def generate_movies(num_movies):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    for _ in range(num_movies):
        # Generate movie details
        title = generate_movie_title()
        release_year = random.randint(1980, 2024)
        rating = round(random.uniform(1, 10), 1)
        description = "A generated movie description."
    
        # Insert movie
        cursor.execute("INSERT INTO Movies (Title, ReleaseYear, Rating, Description, DirectorID) VALUES (?,?,?,?,?)", (title, release_year, rating, description, None,))

    conn.commit()
    conn.close()
