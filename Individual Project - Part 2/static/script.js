// Function to Add Genres
function addGenres() {
    fetch('/api/add_genre', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.text();
    })
    .then(data => {
        console.log('API call succeeded:', data);
        alert('Genre added successfully!');
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        alert('Failed to add genre. Check console for details.');
    });
}

// Function to Add Directors
function addDirectors() {
    fetch('/api/add_director', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.text();
    })
    .then(data => {
        console.log('API call succeeded:', data);
        alert('Director added successfully!');
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        alert('Failed to add director. Check console for details.');
    });
}

// Function to Add Actors
function addActors() {
    fetch('/api/add_actor', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.text();
    })
    .then(data => {
        console.log('API call succeeded:', data);
        alert('Actor added successfully!');
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        alert('Failed to add actor. Check console for details.');
    });
}

// Function to Add Movies
function addMovies() {

    let numberOfMovies = document.getElementById('numberOfMovies').value;

    if (isNaN(numberOfMovies) || numberOfMovies <= 0) {
        alert('Please enter a valid number of movies.');
        return;
    }

    // Send the book data to the server via POST request
    fetch('/api/add_movies', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({numberOfMovies: numberOfMovies})
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.text();
    })
    .then(data => {
        console.log('API call succeeded:', data);
        alert('Movies added successfully!');
        document.getElementById('addedMoviesMessage').textContent = `Sucessfully added: ${numberOfMovies} movies.`;

    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        alert('Failed to add movies. Check console for details.');
    });
}

//Function to Search by Year
function searchYear() {
    let searchYear = document.getElementById('movieYear').value;

    if (isNaN(searchYear) || searchYear <= 0) {
        alert('Please enter a valid search year.');
        return;
    }

    fetch(`/api/search_movies?searchYear=${searchYear}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        console.log('API call succeeded:', data);
        alert('Movies searched successfully!');
        let numberOfMoviesSearched = data.number_of_movies;
        let executionTime = data.execution_time.toFixed(3);
        document.getElementById('moviesFoundByYearMessage').textContent = `Number of movies found: ${numberOfMoviesSearched}`;
        document.getElementById('executionTimeByYear').textContent = `Execution Time: ${executionTime} seconds`;

    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        alert('Failed to fetch movies. Check console for details.');
    });
}


// Function to Search by Year Range
function searchYearRange() {

    let startYear = document.getElementById('startYear').value;
    let endYear = document.getElementById('endYear').value;

    if (isNaN(startYear) || startYear <= 0) {
        alert('Please enter a valid start year.');
        return;
    }

    else if (isNaN(endYear) || endYear <= 0) {
        alert('Please enter a valid end year.');
        return;
    }

    fetch(`/api/search_movies_by_range?startYear=${startYear}&endYear=${endYear}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        console.log('API call succeeded:', data);
        alert('Movies searched successfully!');
        let numberOfMoviesSearched = data.number_of_movies;
        let executionTime = data.execution_time.toFixed(3);
        document.getElementById('moviesFoundByYearRangeMessage').textContent = `Number of movies found: ${numberOfMoviesSearched}`;
        document.getElementById('executionTimeByYearRange').textContent = `Execution Time: ${executionTime} seconds`;

    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        alert('Failed to fetch movies. Check console for details.');
    });
}


