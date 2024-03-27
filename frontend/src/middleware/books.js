import axios from 'axios';

async function booksSearch(bookName) {
    try {
        const response = await axios.post('http://0.0.0.0:5000/api/v1/user/book/search',
            { book_name: bookName },
        );

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
            return null;
        }
    }

export default booksSearch;
