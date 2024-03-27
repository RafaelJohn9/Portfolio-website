import React from 'react';
import NavBar from '../components/CommonComponents/NavBar';

const BookSearch = () => {
    return (
        <div className="min-h-screen flex items-center justify-center bg-gradient-to-tr from-[#c9a26b] to-[#804004] py-12 sm:px-6 lg:px-8 w-full h-screen">
            <NavBar />
            <div className="max-w-md w-full space-y-8">
                <div>
                    <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">
                        Search for a Book
                    </h2>
                </div>
                <form className="mt-8 space-y-6" onSubmit={(e) => { e.preventDefault()}}>
                    <input type="hidden" name="remember" value="true" />
                    <div className="rounded-md shadow-sm -space-y-px">
                        <div>
                            <label htmlFor="book-search" className="sr-only">Book Search</label>
                            <input id="book-search" name="book-search" type="text" required className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm bg-[#c59d65]" placeholder="Book title" />
                        </div>
                    </div>

                    <div>
                        <button type="submit" className="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                            <span className="absolute left-0 inset-y-0 flex items-center pl-3">
                                <svg className="h-5 w-5 text-indigo-500 group-hover:text-indigo-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                                    <path fillRule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm8 2a10 10 0 11-20 0 10 10 0 0120 0z" clipRule="evenodd" />
                                </svg>
                            </span>
                            Search
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
}

export default BookSearch;