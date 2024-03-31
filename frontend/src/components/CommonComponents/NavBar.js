import React from 'react';
import { useState } from 'react';
import { Link } from 'react-router-dom';
import changeLoginStatus from '../../middleware/authentication';

const NavBar = () => {
    const [isOpen, setIsOpen] = useState(false);

    const toggleOpen = () => setIsOpen(!isOpen);

    return (
        <nav className="fixed w-full top-0 z-50 bg-gradient-to-r from-green-800 to-green-900">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex items-center justify-between h-16">
                    <div className="flex items-center">
                        <div className="hidden md:block">
                            <div className="ml-10 flex items-baseline space-x-4">
                                <Link to="/" className="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Home</Link>
                                {console.log(changeLoginStatus().getLoginStatus())}
                               {!changeLoginStatus().getLoginStatus() && <Link to="/login" className="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">SignIn</Link>}
                                <Link to="/about" className="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">About</Link>
                                <Link to="/music-search" className="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Music</Link>
                                <Link to="/movies-search" className="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Movies</Link>
                                <Link to="/books-search" className="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Books</Link>
                            </div>
                        </div>
                    </div>
                    <div className="-mr-2 flex md:hidden">
                        <button onClick={toggleOpen} className="bg-white  bg-opacity-20 inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-white hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-white">
                            <span className="sr-only">Open main menu</span>
                            <svg className={`${isOpen ? 'hidden' : 'block'} h-6 w-6`} xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
                            </svg>
                            <svg className={`${isOpen ? 'block' : 'hidden'} h-6 w-6`} xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                            </svg>
                        </button>
                    </div>
                    <div className="flex self-end lg:gap-14 ml-auto">
                        <a href='https://www.linkedin.com/in/john-kagunda-232961270/' target='_blank' rel='noreferrer'><img width="50" height="50" src="https://img.icons8.com/ios-filled/50/linkedin.png" alt="linkedin" className='rounded-full mb-2'/></a>
                        <a href='https://github.com/RafaelJohn9' target='_blank' rel='noreferrer'><img width="50" height="50" src="https://img.icons8.com/ios-filled/50/github.png" alt="github"/></a>
                        <a href='https://twitter.com/JohnKagunda_12' target='_blank' rel='noreferrer'><img width="50" height="50" src="https://img.icons8.com/ios-filled/50/twitter.png" alt="twitter"/></a>
                    </div>
                </div>
                <div className={`${isOpen ? 'block' : 'hidden'} md:hidden`}>
                    <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3"></div>
                            {!changeLoginStatus().getLoginStatus() && <Link to="/login" className="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">SignIn</Link>}
                            <Link to="/about" className="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">About</Link>
                            <Link to="/music-search" className="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Music</Link>
                            <Link to="/movies-search" className="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Movies</Link>
                            <Link to="/books-search" className="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Books</Link>
                                
                    </div>
                </div>
            </nav>
        );
};

export default NavBar;