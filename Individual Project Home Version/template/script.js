/* 
CSCI 411
Database Theory and Design

file script.js

This program handles the api calls between the html code and the python code. 
Each method in the program corresponds to functionality in the website. 
With some methods making POST requests to change the contents of the database.
And other methods making GET requests to retrieve information from the database.

Based on the action received from the website the program enters the appropriate function.
Then it makes an api call to the python to carry out the POST or GET requests.
Logging all the actions that occur to the console.
And also returning any errors to the console as well.
*/

// Function to Add Genres
function addGenres() {
    //POST request to add a random genre to the database
    fetch('/api/add_genre', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    //error handling to indicate if the response from the website was bad
    .then(response => {  
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.text();
    })
    //error handling to indicate that the response from the website was good
    .then(data => {
        console.log('API call succeeded:', data);
        alert('Genre added successfully!'); // a pop-up appears to inform the user that the genre was successfully added to the database
    })
    // error handling to indicate that there was an issue inserting the genre into the database
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        alert('Failed to add genre. Check console for details.'); // a pop-up appears to inform the user that the genre was not successfully added to the database
    });
}

// Function to Add Directors
function addDirectors() {
    //POST request to add a random director to the database
    fetch('/api/add_director', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    //error handling to indicate if the response from the website was bad
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.text();
    })
    //error handling to indicate that the response from the website was good
    .then(data => {
        console.log('API call succeeded:', data);
        alert('Director added successfully!'); // a pop-up appears to inform the user that the director was successfully added to the database.
    })
    // error handling to indicate that there was an issue inserting the director into the database
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        alert('Failed to add director. Check console for details.'); // a pop-up appears to inform the user that the director was not successfully added to the database.
    });
}

// Function to Add Actors
function addActors() {
    //POST request to add a random actor to the database
    fetch('/api/add_actor', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    //error handling to indicate if the response from the website was bad
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.text();
    })
    //error handling to indicate that the response from the website was good
    .then(data => {
        console.log('API call succeeded:', data);
        alert('Actor added successfully!'); // a pop-up appears to inform the user that the actor was successfully added to the database.
    })
    // error handling to indicate that there was an issue inserting the actor into the database
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        alert('Failed to add actor. Check console for details.'); // a pop-up appears to inform the user that the actor was not successfully added to the database.
    });
}

// Function to Add Movies
function addMovies() {

    let numberOfMovies = document.getElementById('numberOfMovies').value; //input received from the website to indicate how many movies to generate

    //error handling to prevent the user from entering a negitive value
    if (isNaN(numberOfMovies) || numberOfMovies <= 0) {
        alert('Please enter a valid number of movies.');
        return;
    }

    //POST request to add a specified amount of random movies to the database
    fetch('/api/add_movies', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({numberOfMovies: numberOfMovies})
    })
    //error handling to indicate if the response from the website was bad
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.text();
    })
    //error handling to indicate that the response from the website was good
    .then(data => {
        console.log('API call succeeded:', data);
        alert('Movies added successfully!'); // a pop-up appears to inform the user that the movies have been successfully added to the database.
        document.getElementById('addedMoviesMessage').textContent = `Sucessfully added: ${numberOfMovies} movies.`; // text on the website appears to indicate how many movies have been added to the database

    })
    //error handling to indicate that there was an issue inserting the movies into the database
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        alert('Failed to add movies. Check console for details.'); // a pop-up appears to inform the user that the movies was not successfully added to the database.
    });
}

//Function to Search by Year
function searchYear() {
    let searchYear = document.getElementById('movieYear').value; //input received from the website to indicate what year to search movies by

    //error handling to prevent the user from entering a negitive value
    if (isNaN(searchYear) || searchYear <= 0) {
        alert('Please enter a valid search year.');
        return;
    }

    //GET request to search for a movie based on the specified year
    fetch(`/api/search_movies?searchYear=${searchYear}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    })
    //error handling to indicate if the response from the website was bad
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    //error handling to indicate if the response from the website was good
    .then(data => {
        console.log('API call succeeded:', data);
        alert('Movies searched successfully!'); // a pop-up appears to inform the user that database was successfully searched
        let numberOfMoviesSearched = data.number_of_movies; // setting the "numberOfMoviesSearched" varible to the amount of movies retrieved from the database
        let executionTime = data.execution_time.toFixed(3); // setting the "executionTime" varible to the amount time in seconds that it took to retrieve the movies from the database
        document.getElementById('moviesFoundByYearMessage').textContent = `Number of movies found: ${numberOfMoviesSearched}`; // text on the website appears to indicate how many movies have been found in the database
        document.getElementById('executionTimeByYear').textContent = `Execution Time: ${executionTime} seconds`; // text on the website appears to indicate how much time in seconds that it took to retrieve the movies from the database

    })
    //error handling to indicate that there was an issue retrieving the movies from the database
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        alert('Failed to fetch movies. Check console for details.');// a pop-up appears to inform the user that the movies were unable to be retrieved from the database
    });
}


// Function to Search by Year Range
function searchYearRange() {

    let startYear = document.getElementById('startYear').value; // the starting value of the range of years to be searched specified by the user
    let endYear = document.getElementById('endYear').value; // then ending value of the range of years to be searched specified by the user

    //error handling to prevent the user from entering a negitive value
    if (isNaN(startYear) || startYear <= 0) {
        alert('Please enter a valid start year.');
        return;
    }

    //error handling to prevent the user from entering a negitive value
    else if (isNaN(endYear) || endYear <= 0) {
        alert('Please enter a valid end year.');
        return;
    }

    //GET request to search for a movie based on the specified year
    fetch(`/api/search_movies_by_range?startYear=${startYear}&endYear=${endYear}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    })
    //error handling to indicate if the response from the website was bad
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    //error handling to indicate if the response from the website was good
    .then(data => {
        console.log('API call succeeded:', data);
        alert('Movies searched successfully!');
        let numberOfMoviesSearched = data.number_of_movies; // setting the "numberOfMoviesSearched" varible to the amount of movies retrieved from the database
        let executionTime = data.execution_time.toFixed(3); // setting the "executionTime" varible to the amount time in seconds that it took to retrieve the movies from the database
        document.getElementById('moviesFoundByYearRangeMessage').textContent = `Number of movies found: ${numberOfMoviesSearched}`; // text on the website appears to indicate how many movies have been found in the database
        document.getElementById('executionTimeByYearRange').textContent = `Execution Time: ${executionTime} seconds`;  // text on the website appears to indicate how much time in seconds that it took to retrieve the movies from the database

    })
    //error handling to indicate that there was an issue retrieving the movies from the database
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        alert('Failed to fetch movies. Check console for details.'); // a pop-up appears to inform the user that the movies were unable to be retrieved from the database
    });
}


