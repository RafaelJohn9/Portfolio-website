import axios from 'axios';

async function login(user) {
    const { email, password } = user;
    try {
        const response = await axios.post('https://www.johnmkagunda.me/api/v1/skills', { email, password });
        
        
        return { ...response}; // Include the token in the response
    } catch (error) {
        return { status: 500, message: 'Server error' };
    }
}

export default login;
