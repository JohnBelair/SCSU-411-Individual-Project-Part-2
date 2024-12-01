#CSCI 411
#Database Theory and Design
#
#file app.py
#
# This program handles all the api calls sent by the script.js file/
# All of the set_* methods call another file helper.py 
# which contains all the code to generate each attribute of the database.
# The get_* methods handle the database retreval within themselves.
#
#
# When ran the app.py uses flask to create a webserver
# that utilizes the database stored the db folder.
# The default route of the webserver uses the idex.html file
# to provide a UI for the user to interact with.


from flask import Flask, jsonify, render_template, request
import helper
import sqlite3
import time

app = Flask(__name__)

# Define the path to your SQLite database file
DATABASE = 'db/movies.db'

# API call to add a genre to the database
@app.route('/api/add_genre', methods=['POST'])
def set_genre():
    try:
        #setting up the connection to the database and the cursor to parse through it
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        
        GenreName = helper.generate_genre()  # generate the GenreName by calling the generate_genre() method in helper.py

        #execute the sql command and commit the changes to the database
        cursor.execute("INSERT INTO Genres (GenreName) VALUES (?)", (GenreName,))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Genre added successfully'}) # returning a message to the console that the genre was added to the database
    
    # execption handler to tell the user if there was an error adding the genre to the database
    except Exception as e:
        app.logger.error(f"Error adding genre: {e}") # returning a message to the console that the genre was unable to be added to the database
        return jsonify({'error': str(e)})

# API call to add a director to the database
@app.route('/api/add_director', methods=['POST'])
def set_director():
    try:
        #setting up the connection to the database and the cursor to parse through it
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        Director = helper.generate_director() # generate the Director by calling the generate_director() method in helper.py
        director_name, birth_date = Director  # unpack the tuple

        #execute the sql command and commit the changes to the database
        cursor.execute("INSERT INTO Directors (DirectorName, BirthDate) VALUES (?,?)", (director_name, birth_date, ))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Director added successfully'}) # returning a message to the console that the director was added to the database
    
    # execption handler to tell the user if there was an error adding the director to the database
    except Exception as e:
        app.logger.error(f"Error adding director: {e}") # returning a message to the console that the director was unable to be added to the database
        return jsonify({'error': str(e)})

# API call to add an actor to the database    
@app.route('/api/add_actor', methods=['POST'])
def set_actor():
    try:
        #setting up the connection to the database and the cursor to parse through it
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        Actor = helper.generate_actor() # generate the Actor by calling the generate_actor() method in helper.py
        actor_name, birth_date = Actor  # unpack the tuple

        #execute the sql command and commit the changes to the database
        cursor.execute("INSERT INTO Actors (ActorName, BirthDate) VALUES (?,?)", (actor_name, birth_date, ))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Actor added successfully'}) # returning a message to the console that the actor was added to the database
    
    # execption handler to tell the user if there was an error adding the director to the database
    except Exception as e:
        app.logger.error(f"Error adding actor: {e}") # returning a message to the console that the actor was unable to be added to the database
        return jsonify({'error': str(e)})

# API call to add movies to the database   
@app.route('/api/add_movies', methods=['POST'])
def set_movies():
    try:
        # getting the numberOfMovies from the json file to recieve the input from the website's textbox
        data = request.get_json()
        number_of_movies = data.get('numberOfMovies')

        #implicit conversion into an int so it can be passed into the generate_movies() method
        num_movies = int(number_of_movies)

        # generate the movies by calling the generate_movies() method in helper.py
        helper.generate_movies(num_movies)

        # returning a message to the console that the movies were added to the database
        return jsonify({'message': 'Movies added successfully'})
    
     # execption handler to tell the user if there was an error adding the movies to the database
    except Exception as e:
        app.logger.error(f"Error adding movies: {e}") # returning a message to the console that the movies were unable to be added to the database
        return jsonify({'error': str(e)})
    
# API call to search for movies in the database   
@app.route('/api/search_movies', methods=['GET'])
def get_movies():
    try:
        #setting up the connection to the database and the cursor to parse through it
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # getting the searchYear from the arguments to recieve the input from the website's textbox
        search_year = request.args.get('searchYear', type=int)
        
        start_time = time.time() #getting timer time to calcuate the time it took to preform the SQL
        cursor.execute("SELECT COUNT(*) FROM Movies WHERE ReleaseYear = ?", (search_year,)) # SQL to be executed on the database
        result = cursor.fetchone()  # fetch the result from the SQL
        movie_count = result[0] if result else 0 # Extract the count from the result
        end_time = time.time() #get the timer time to calcuate the time it took to preform the SQL
        execution_time = (end_time - start_time) #calculating the time it took to preform the SQL

        #generating a response to return to the script.js file
        response = {
            'message': 'Movies found successfully',
            "number_of_movies": movie_count,
            "execution_time" : execution_time,
        }

        #returning the response to the script.js file
        return jsonify(response)
    
    #execption handler to tell the user if there was an error retreiving the movies from the database
    except Exception as e:
        app.logger.error(f"Error finding movies: {e}") # returning a message to the console that the movies were unable to be retrieved from the database
        return jsonify({'error': str(e)})

# API call to search for movies in the database by range   
@app.route('/api/search_movies_by_range', methods=['GET'])
def get_movies_by_range():
    try:
        #setting up the connection to the database and the cursor to parse through it
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        
        start_year = request.args.get('startYear', type=int) # getting the startYear from the arguments to recieve the input from the website's textbox
        end_year = request.args.get('endYear', type=int) # getting the endYear from the arguments to recieve the input from the website's textbox

        start_time = time.time() #getting timer time to calcuate the time it took to preform the SQL
        cursor.execute("SELECT COUNT(*) FROM Movies WHERE ReleaseYear >= ? AND ReleaseYear <= ?", (start_year, end_year)) # SQL to be executed on the database
        result = cursor.fetchone()  # fetch the result from the SQL
        movie_count = result[0] if result else 0 # Extract the count from the result
        end_time = time.time() #get the timer time to calcuate the time it took to preform the SQL
        execution_time = (end_time - start_time) #calculating the time it took to preform the SQL

        #generating a response to return to the script.js file
        response = {
            'message': 'Movies found successfully',
            "number_of_movies": movie_count,
            "execution_time" : execution_time,
        }
        
        #returning the response to the script.js file
        return jsonify(response)
    
    #execption handler to tell the user if there was an error retreiving the movies from the database
    except Exception as e:
        app.logger.error(f"Error finding movies: {e}") # returning a message to the console that the movies were unable to be retrieved from the database
        return jsonify({'error': str(e)})

# Route to render the index.html page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
