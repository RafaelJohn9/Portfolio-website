import React, { useState } from 'react';
import NavBar from '../components/CommonComponents/NavBar';
import BackGroundImage from '../imgs/login_background_image.jpg';
import GoogleLogo from '../imgs/Google_logo.svg';
import EyeIcon from '../imgs/eye.svg';
import EyeOffIcon from '../imgs/eyeOff.svg';
import { Link, useNavigate } from 'react-router-dom';
import { login } from '../middleware/user';
import changeLoginStatus from '../middleware/authentication';

const LoginPage = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState(null);
    const navigate = useNavigate();

    const handleLogin = async (e) => {
        e.preventDefault();
        try {
            const response = await login({email, password});
            if (response.status === 200) {
                changeLoginStatus().setLoginStatus(true);
                // Navigate back to the homepage if login is successful
                navigate('/');
            } else if (response.status === 401) {
                setError('Invalid password. Please try again.');
            } else if (response.status === 404) {
                setError('Email not found. Please check your email address.');
            } else {
                setError('An error occurred while logging in.');
            }
        } catch (error) {
            console.error('Error:', error);
            if (error.response && error.response.status === 404) {
                setError('Email not found. Please check your email address.');
            } else if (error.response && error.response.status === 401) {
                setError('Invalid password. Please try again.');
            } else {
                setError('An error occurred while logging in.');
            }
        }
    };

    const handleGoogleLogin = () => {
        changeLoginStatus().setLoginStatus(true);
        // Redirect to Google login page
        changeLoginStatus().setLoginStatus(true);
        window.location.href = 'http://localhost:5000/api/v1/user/google';
    };

    const [showPassword, setShowPassword] = useState(false);

    const togglePasswordVisibility = () => {
        setShowPassword(!showPassword);
    };

    return (
        <div className="min-h-screen flex items-center justify-center bg-gradient-to-tr from-green-900 to-green-300" style={{backgroundImage: `url(${BackGroundImage})`}}>
            <NavBar />
            <div className="w-full h-full max-w-xs">
                <form onSubmit={handleLogin} className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
                    <div className="mb-4">
                        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="username">
                            Email
                        </label>
                        <input
                            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                            id="username"
                            type="text"
                            required
                            placeholder="Email"
                            maxLength="100"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                        />
                    </div>
                    <div className="mb-6">
                        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="password">
                            Password
                        </label>
                        <div className='flex shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline'>
                        <input
                            className='outline-none'
                            id="password"
                            type={showPassword ? "text" : "password"}
                            required
                            placeholder="******************"
                            maxLength="100"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                        <button onClick={togglePasswordVisibility} type="button" className='w-2/12' >
                            <img src={showPassword ? EyeOffIcon : EyeIcon} alt="toggle visibility" />
                        </button>
                        </div>
                    </div>
                    <div className="flex items-center justify-between">
                        <button
                            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                            type="submit"
                        >
                            Sign In
                        </button>
                        <button
                            className="hover:bg-gray-300 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                            onClick={handleGoogleLogin}
                            type="button"
                        >
                            <img src={GoogleLogo} alt="Google logo" className="w-6 h-6 hover:text-red-600 transition-colors duration-200"/>
                        </button>
                    </div>
                    {error && <div className="text-red-500">{error}</div>}
                </form>
                <div className="mt-4">
                    <Link to="/register" className="text-black hover:text-green-400 transition-colors duration-200">
                        Don't have an account yet? Register
                    </Link>
                </div>
            </div>
        </div>
    );
}

export default LoginPage;
