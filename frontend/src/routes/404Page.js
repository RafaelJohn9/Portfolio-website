import React from 'react';
import { Link } from 'react-router-dom';

const NotFoundPage = () => {
    return (
        <div className="min-h-screen flex items-center justify-center bg-gradient-to-tr from-[#19b884] to-green-600">
            <div className="text-center">
                <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHlpcXliOHdpYTJrcHowZGw3YW11c21ndjMzeGw1eHl0ZzYwZHc4YiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/UgRfRYyNnQlLXUoLk3/200.webp" alt=""/>
                <h1 className="text-6xl font-semibold text-white">404</h1>
                <p className="text-xl text-white mt-4">We couldn't find what you were looking for.</p>
                <p className="text-white mt-2">Please check the URL or go back to the <Link to="/"><p className='text-blue-500'>Homepage.</p></Link></p>
            </div>
        </div>
    );
};

export default NotFoundPage;