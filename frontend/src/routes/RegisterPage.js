import React from 'react';
import NavBar from '../components/CommonComponents/NavBar';
import BackGroundImage from '../imgs/login_background_image.jpg'
import GoogleLogo from '../imgs/Google_logo.svg'

const LoginPage = () => {
    const [email, setEmail] = React.useState("");
    const [password, setPassword] = React.useState("");
    const [confirmPassword, setConfirmPassword] = React.useState("");

    const handleSubmit = (event) => {
        event.preventDefault();
        if (password !== confirmPassword) {
            alert("Passwords do not match!");
            return;
        }
        // Submit form logic here
        console.log(`Email: ${email}, Password: ${password}`);
    };

    return (
        <div className="min-h-screen flex items-center justify-center bg-gradient-to-tr from-green-900 to-green-300" style={{backgroundImage: `url(${BackGroundImage})`}}>
            <NavBar />
            <div className="w-full h-full max-w-xs">
                <form className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 bg-opacity-70" onSubmit={handleSubmit}>
                    <div className="mb-4">
                        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="username">
                            Email
                        </label>
                        <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)}/>
                    </div>
                    <div className="mb-6">
                        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="password">
                            Password
                        </label>
                        <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" id="password" type="password" placeholder="******************" value={password} onChange={(e) => setPassword(e.target.value)}/>
                    </div>
                    <div className="mb-6">
                        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="confirmPassword">
                            Confirm Password
                        </label>
                        <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline" id="confirmPassword" type="password" placeholder="******************" value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)}/>
                    </div>
                    <div className="flex items-center justify-between">
                        <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">
                            Sign Up
                        </button>
                        <p className='font-custome font-extrabold'>&nbsp;&nbsp;&nbsp;or&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use</p>
                        <button className=" hover:bg-gray-300 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="button">
                            <img src={GoogleLogo} alt="Google logo" className="w-6 h-6 hover:text-red-600 transition-colors duration-200"/>
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
}

export default LoginPage;