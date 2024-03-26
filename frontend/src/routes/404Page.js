import React from 'react';
import { Link } from 'react-router-dom';

const NotFoundPage = () => {
    return (
        <div className="min-h-screen flex items-center justify-center bg-gradient-to-tr from-green-900 to-green-100">
            <div className="text-center">
                <h1 className="text-6xl font-semibold text-white">404</h1>
                <p className="text-xl text-white mt-4">We couldn't find what you were looking for.</p>
                <p className="text-white mt-2">Please check the URL or go back to the <Link to="/"><p className='text-blue-500'>Homepage.</p></Link></p>
            </div>
        </div>
    );
};

export default NotFoundPage;