import axios from 'axios';

async function moviesSearch(movieName) {
    try {
        const instance = axios.create({
            baseURL: 'https://www.johnmkagunda.me/api/v1/user/movie'
        });

        const response = await instance.post('/search', { movie_name: movieName });

        // If response status is 200, return the JSON data
        if (response.status === 200) {
            return response.data;
        } else {
            // Handle unexpected status codes
            throw new Error(`Unexpected status code: ${response.status}`);
        }
        } catch (error) {
            // Handle network errors or errors from the server
            if (error.response) {
                // The request was made and the server responded with a status code
                // that falls out of the range of 2xx
                console.error('Error response from server:', error.response.data);
            } else if (error.request) {
                // The request was made but no response was received
                console.error('No response received:', error.request);
            } else {
                // Something happened in setting up the request that triggered an Error
                console.error('Error setting up the request:', error.message);
            }
            // Return null or handle error response as needed
            return [];
        }
    }

export default moviesSearch;
