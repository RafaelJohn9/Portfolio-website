# User API Endpoints

This document provides detailed descriptions for the User API endpoints.

## POST /create

This endpoint is used to create a new user. It accepts a JSON object with `username`, `email`, and `password` fields.

If a user with the provided email or username already exists, the server will respond with a 409 Conflict status code and a JSON object containing an error message.

On successful creation, the server responds with a 201 Created status code and a JSON object containing a success message and the details of the newly created user.

## PUT /update/<string:userId>

This endpoint is used to update an existing user. It accepts a JSON object with `username`, `email`, and `password` fields.

If a user with the provided userId does not exist, the server will respond with a 404 Not Found status code and a JSON object containing an error message.

If a user with the provided email or username already exists, the server will respond with a 409 Conflict status code and a JSON object containing an error message.

On successful update, the server responds with a 200 OK status code and a JSON object containing a success message and the details of the updated user.

## DELETE /delete/<string:userId>

This endpoint is used to delete an existing user.

If a user with the provided userId does not exist, the server will respond with a 404 Not Found status code and a JSON object containing an error message.

On successful deletion, the server responds with a 200 OK status code and a JSON object containing a success message.

## GET /fetch/<string:userId>

This endpoint is used to fetch the details of an existing user.

If a user with the provided userId does not exist, the server will respond with a 404 Not Found status code and a JSON object containing an error message.

On successful fetch, the server responds with a 200 OK status code and a JSON object containing the details of the fetched user.


## OAuth /google

This endpoint is used to authenticate a user using Google's OAuth service. It redirects the user to Google's authorization page.

If an error occurs during the process, the server will respond with an error message.

## OAuth /google/authorized

This endpoint is used to handle the callback from Google's OAuth service after user authentication. It receives the user's access token and uses it to fetch the user's email from Google's userinfo endpoint.

If the user's email does not exist in the system, a new user is created with the fetched email. The user is then logged in and redirected to the dashboard.

If an error occurs during the process, the server will respond with an error message.

## OAuth Token Getter

This function is used to get the user's Google OAuth token from the session. If an error occurs during the process, the server will respond with an error message.


## POST /login

This endpoint is used to log in a user. It accepts a JSON object with `email` and `password` fields.

If the `email` or `password` field is missing, the server will respond with a 400 Bad Request status code and a JSON object containing an error message.

If a user with the provided email does not exist, the server will respond with a 404 Not Found status code and a JSON object containing an error message.

If the provided password does not match the user's password, the server will respond with a 401 Unauthorized status code and a JSON object containing an error message.

On successful login, the server responds with a 302 Found status code and redirects the user to the dashboard.

## POST /logout

This endpoint is used to log out a user.

On successful logout, the server responds with a 302 Found status code and redirects the user to the homepage with a success message.
## POST /music/recommend

This endpoint is used to recommend music. It accepts a JSON object with `track_name`, `item_type`, and `Release date` fields.

If the user is not authenticated, the server will redirect to the login page.

On successful recommendation, the server responds with a 200 OK status code and a JSON object containing a success message.

## POST /movie/recommend

This endpoint is used to recommend movies. It accepts a JSON object with `title`, `item_type`, and `release_date` fields.

If the user is not authenticated, the server will redirect to the login page.

On successful recommendation, the server responds with a 200 OK status code and a JSON object containing a success message.

## POST /book/recommend

This endpoint is used to recommend books. It accepts a JSON object with `title`, `item_type`, and `release_date` fields.

If the user is not authenticated, the server will redirect to the login page.

On successful recommendation, the server responds with a 200 OK status code and a JSON object containing a success message.


## GET /music/recommended

This endpoint is used to get recommended music for a user. It accepts a JSON object with `user_id` field.

If the user is not authenticated, the server will redirect to the login page.

On successful fetch, the server responds with a 200 OK status code and a JSON object containing the recommended music.

## GET /movie/recommended

This endpoint is used to get recommended movies for a user. It accepts a JSON object with `user_id` field.

If the user is not authenticated, the server will redirect to the login page.

On successful fetch, the server responds with a 200 OK status code and a JSON object containing the recommended movies.

## GET /book/recommended

This endpoint is used to get recommended books for a user. It accepts a JSON object with `user_id` field.

If the user is not authenticated, the server will redirect to the login page.

On successful fetch, the server responds with a 200 OK status code and a JSON object containing the recommended books.

## GET /book/all-recommended

This endpoint is used to get all recommended books.

If the user is not authenticated, the server will redirect to the login page.

On successful fetch, the server responds with a 200 OK status code and a JSON object containing all the recommended books.

## GET /music/all-recommended

This endpoint is used to get all recommended music.

If the user is not authenticated, the server will redirect to the login page.

On successful fetch, the server responds with a 200 OK status code and a JSON object containing all the recommended music.

## GET /movie/all-recommended

This endpoint is used to get all recommended movies.

If the user is not authenticated, the server will redirect to the login page.

On successful fetch, the server responds with a 200 OK status code and a JSON object containing all the recommended movies.

## POST /music/search

This endpoint is used to search for music. It accepts a JSON object with `music_name` field.

If an error occurs during the process, the server will respond with a 400 Bad Request status code and a JSON object containing an error message.

On successful search, the server responds with a 200 OK status code and a JSON object containing the search results.

## POST /movie/search

This endpoint is used to search for movies. It accepts a JSON object with `movie_name` field.

If an error occurs during the process, the server will respond with a 400 Bad Request status code and a JSON object containing an error message.

On successful search, the server responds with a 200 OK status code and a JSON object containing the search results.

## POST /book/search

This endpoint is used to search for books. It accepts a JSON object with `book_name` field.

If an error occurs during the process, the server will respond with a 400 Bad Request status code and a JSON object containing an error message.

On successful search, the server responds with a 200 OK status code and a JSON object containing the search results.
## GET /dashboard

This endpoint is used to get the current user's dashboard. It does not require any parameters.

If the user is not authenticated, the server will redirect to the homepage with a message "Unauthorized access".

On successful fetch, the server responds with a 200 OK status code and a JSON object containing the user's information.
