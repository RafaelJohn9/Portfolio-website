import React from 'react';
import NavBar from '../components/CommonComponents/NavBar';
import BackGroundImage from '../imgs/login_background_image.jpg'
import GoogleLogo from '../imgs/Google_logo.svg'
import EyeIcon from '../imgs/eye.svg';
import EyeOffIcon from '../imgs/eyeOff.svg';
import {createUser, login} from '../middleware/user';
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';
import changeLoginStatus from '../middleware/authentication';

const LoginPage = () => {
    const [username, setUsername] = React.useState("");
    const [email, setEmail] = React.useState("");
    const [password, setPassword] = React.useState("");
    const [confirmPassword, setConfirmPassword] = React.useState("");
    const [errorMessage, setErrorMessage] = React.useState(null);
    const navigate = useNavigate();

    const handleGoogleLogin = () => {
        // Redirect to Google login page
        changeLoginStatus().setLoginStatus(true);
        window.location.href = 'https://www.johnmkagunda.me/api/v1/user/google';
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        if (password !== confirmPassword) {
            alert("Passwords do not match!");
            return;
        }
        createUser({ username, email, password })
            .then(response => {
                // Display success message
                let isSuccessfull = false;
                if (response.status === 409){
                    setErrorMessage(response.message)
                }else{
                    isSuccessfull = true;                    
                }
                if (!isSuccessfull) return;
                // Call the login function
                login({ email, password })
                    .then(loginResponse => {
                        // If login is successful, reroute to homepage
                        console.log(loginResponse)
                        if (loginResponse.status === 200) {
                            changeLoginStatus().setLoginStatus(true)
                            navigate('/');
                        } else {
                            // If login fails, set an error state that will be rendered if not null
                            setErrorMessage(loginResponse.message);
                        }
                    })
                    .catch(loginError => {
                        // If login fails, remain on the page and display the error message
                        console.error(loginError.message);
                    });
            })
            .catch(error => {
                // Display error message
                console.error(error.message);
            });
    };

    // Used to show password visibility
    const [showPassword, setShowPassword] = useState(false);

    const togglePasswordVisibility = () => {
        setShowPassword(!showPassword);
    };

    const [showConfirmPassword, setShowConfirmPassword] = useState(false);

    const toggleConfirmPasswordVisibility = () => {
        setShowConfirmPassword(!showConfirmPassword);
    };

    return (
        <div className="min-h-screen flex items-center justify-center bg-gradient-to-tr from-green-900 to-green-300" style={{backgroundImage: `url(${BackGroundImage})`}}>
            <NavBar />
            <div className="w-full h-full max-w-xs form-container">
                <form className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 bg-opacity-70" onSubmit={handleSubmit}>
                   <div className="mb-4">
                        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="username">
                            Username
                        </label>
                        <input required className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value.slice(0, 100))}/>
                    </div>
                    <div className="mb-4">
                        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="email">
                            Email
                        </label>
                        <input required className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="email" type="text" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value.slice(0, 100))}/>
                    </div>
                    <div className="mb-6">
                        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="password">
                            Password
                        </label>
                        <div className='bg-white flex shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline'>
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
                            <img src={showPassword ? EyeOffIcon : EyeIcon} alt="" />
                        </button>
                    </div>
                    </div>
                    <div className="mb-6">
                        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="confirmPassword">
                            Confirm Password
                        </label>
                        <div className='flex bg-white shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline'>
                        <input 
                                required 
                                className="focus:outline-none" 
                                id="confirmPassword" 
                                type={showConfirmPassword ? "text" : "password"}
                                placeholder="******************" 
                                value={confirmPassword} 
                                onChange={(e) => setConfirmPassword(e.target.value.slice(0, 100))}
                                />
                        <button onClick={toggleConfirmPasswordVisibility} type="button" className='w-2/12'>
                            <img src={showConfirmPassword ? EyeOffIcon : EyeIcon} alt=""/>
                        </button>
                        </div>
                    </div>
                    <div className="flex items-center justify-between">
                        <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">
                            Sign Up
                        </button>
                        <p className='font-custome font-extrabold'>&nbsp;&nbsp;&nbsp;or&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use</p>
                        <button className=" hover:bg-gray-300 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="button" onClick={handleGoogleLogin}>
                            <img src={GoogleLogo} alt="Google logo" className="w-6 h-6 hover:text-red-600 transition-colors duration-200"/>
                        </button>
                    </div>
                   {errorMessage && (
                     <div className="w-full h-10  text-red-800">
                          {errorMessage}
                      </div>
                   )}
            </form>
            </div>
        </div>
    );
}

export default LoginPage;
