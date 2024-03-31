import axios from 'axios';

axios.defaults.withCredentials = true; // Include credentials with requests


async function login(user) {
    const { email, password } = user;
    try {
        const response = await axios.post('http://localhost:5000/api/v1/user/login', { email, password });
        
        
        return { ...response}; // Include the token in the response
    } catch (error) {
        return { status: 500, message: 'Server error' };
    }
}

export default login;
