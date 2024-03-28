/* eslint-disable no-useless-escape */
import axios from 'axios';

function validateEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

async function createUser(user) {
    const { username, email, password } = user;

    if (!validateEmail(email)) {
        return { status: 400, message: 'Invalid email format' };
    }

    try {
        const response = await axios.post('http://localhost:5000/api/v1/user/create', { username, email, password });

        if (response.status === 201) {
            return { status: 201, message: 'Successfully created user' };
        }
    } catch (error) {
        if (error.response && error.response.status === 409) {
            return { status: 409, message: 'Email already in use' };
        } else {
            return { status: 500, message: 'Server error' };
        }
    }
}

async function login(user) {
    const { email, password } = user;
    try {
        const response = await axios.post('http://localhost:5000/api/v1/user/login', { email, password });
        return response;
    } catch (error) {
        return { status: 500, message: 'Server error' };
    }
}



export { createUser, login };