from flask import Flask, jsonify, render_template, request
import helper
import sqlite3
import time

app = Flask(__name__)

# Define the path to your SQLite database file
DATABASE = 'db/movies.db'

@app.route('/api/add_genre', methods=['POST'])
def set_genre():
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Insert the Genre into the database
        GenreName = helper.generate_genre()  # Generate the GenreName
        cursor.execute("INSERT INTO Genres (GenreName) VALUES (?)", (GenreName,))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Genre added successfully'})
    except Exception as e:
        app.logger.error(f"Error adding genre: {e}")
        return jsonify({'error': str(e)})

@app.route('/api/add_director', methods=['POST'])
def set_director():
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Insert the Director into the database
        Director = helper.generate_director() # Generate the Director
        director_name, birth_date = Director  # Unpack the tuple

        cursor.execute("INSERT INTO Directors (DirectorName, BirthDate) VALUES (?,?)", (director_name, birth_date, ))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Director added successfully'})
    except Exception as e:
        app.logger.error(f"Error adding director: {e}")
        return jsonify({'error': str(e)})
    
@app.route('/api/add_actor', methods=['POST'])
def set_actor():
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Insert the Actor into the database
        Actor = helper.generate_actor() # Generate the Actor
        actor_name, birth_date = Actor  # Unpack the tuple

        cursor.execute("INSERT INTO Actors (ActorName, BirthDate) VALUES (?,?)", (actor_name, birth_date, ))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Actor added successfully'})
    except Exception as e:
        app.logger.error(f"Error adding actor: {e}")
        return jsonify({'error': str(e)})

@app.route('/api/add_movies', methods=['POST'])
def set_movies():
    try:
        data = request.get_json()
        number_of_movies = data.get('numberOfMovies')

        num_movies = int(number_of_movies)

        # Insert the Movies into the database
        helper.generate_movies(num_movies)
        return jsonify({'message': 'Movies added successfully'})
    except Exception as e:
        app.logger.error(f"Error adding movies: {e}")
        return jsonify({'error': str(e)})
    

@app.route('/api/search_movies', methods=['GET'])
def get_movies():
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        search_year = request.args.get('searchYear', type=int)

        start_time = time.time()
        cursor.execute("SELECT COUNT(*) FROM Movies WHERE ReleaseYear = ?", (search_year,))
        result = cursor.fetchone()  # Fetch the result
        movie_count = result[0] if result else 0 # Extract the count from the result
        end_time = time.time()
        execution_time = (end_time - start_time)

        response = {
            'message': 'Movies found successfully',
            "number_of_movies": movie_count,
            "execution_time" : execution_time,
        }

        return jsonify(response)
    
    except Exception as e:
        app.logger.error(f"Error finding movies: {e}")
        return jsonify({'error': str(e)})

@app.route('/api/search_movies_by_range', methods=['GET'])
def get_movies_by_range():
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        start_year = request.args.get('startYear', type=int)
        end_year = request.args.get('endYear', type=int)

        start_time = time.time()
        cursor.execute("SELECT COUNT(*) FROM Movies WHERE ReleaseYear >= ? AND ReleaseYear <= ?", (start_year, end_year))
        result = cursor.fetchone()  # Fetch the result
        movie_count = result[0] if result else 0 # Extract the count from the result
        end_time = time.time()
        execution_time = (end_time - start_time)

        response = {
            'message': 'Movies found successfully',
            "number_of_movies": movie_count,
            "execution_time" : execution_time,
        }

        return jsonify(response)
    
    except Exception as e:
        app.logger.error(f"Error finding movies: {e}")
        return jsonify({'error': str(e)})

# Route to render the index.html page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
