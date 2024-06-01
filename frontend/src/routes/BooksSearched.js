/**
 * display page for searched books
 */
import React, { useState, useEffect } from 'react';
import booksSearch from '../middleware/books';
import { useLocation, useNavigate } from 'react-router-dom';
import recommend from '../middleware/recommend';
// Importing necessary libraries and components

// Component to fetch and display books based on the search query
const GetBooks = ({ query }) => {
    // State variables for books, error and loading status
    const [books, setBooks] = useState([]);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(true);



    // Fetch books when component mounts or query changes
    useEffect(() => {
        const fetchBooks = async () => {
            try {
                const data = await booksSearch(query);
                setBooks(data);
            } catch (error) {
                setError(error.message);
            }
            setTimeout(() => {
                setLoading(false);
            }, 5000);
        };
        fetchBooks();
    }, [query]);

    // Show loading message
    if (loading) {
        return <div>Loading...</div>;
    }

    // Show error message
    if (error) {
        return <div>Error: {error}</div>;
    }

    // Display books or no results message
    return (
        <div className='text-[#fa3329] italic font-custom flex flex-wrap gap-32 items-center justify-center'>
            {books.length === 0 ? (
                <h1 className='text-4xl'>No results found</h1>
            ) : (
                books.map((book, index) => {
                    if (!book.cover_images || book.cover_images.thumbnail === 'N/A') {
                        return null;
                    }
                    return (
                        <div key={index} className='mt- bg-opacity-30 bg-[#7c3131bb] flex flex-wrap w-full md:w-2/5 lg:w-2/6 p-8 rounded-xl'>
                            <div className='flex'>
                                <img src={book.cover_images.thumbnail} alt="" />
                                <div className='flex flex-wrap text-black flex-col pl-4 pt-4'>
                                    <h1 className='text-center font-extrabold pb-3 pr-2'>Title: {book.title}</h1>
                                    {book.rating && (
                                        <div className='flex'>
                                        <h2 className='font-bold text-lg'>Rating:</h2>
                                        <p className='pl-8 font-bold'>{book.rating} /10 </p>
                                        </div>
                                    )}
                                    <p className='font-bold'>Author: {book.authors} </p>
                                </div>
                            </div>
                            <div className='flex w-full items-center justify-center'>
                                    <button className='bg-red-600 font-custom hover:bg-red-800 rounded-full text-black flex p-4 my-5   text-center' onClick={async (event) => {
                                        event.target.innerText = 'Recommended';
                                        await recommend(book);
                                    }}>Recommend</button>
                            </div>
                        </div>
                    );
                })
            )}
        </div>
    );
};

// Main component for searching books
const BooksSearched = () => {
    // Hooks for location and navigation and search handler
    const location = useLocation();
    const navigate = useNavigate();
    const [clickedSearch, setClickedSearch] = useState(false);
    const [search, setSearch] = useState('');




    // Extracting search query from the URL
    const query = location.pathname.split('/')[2].replace(/-/g, ' '); 

    // State variables for search term and error message
    const [errorMessage, setErrorMessage] = useState('');

    // Handler for search input change
    const handleSearchChange = (event) => {
        setSearch(event.target.value);
    };

    // Handler for search action
    const handleSearch = () => {
        if (search === '') {
            setErrorMessage('Please fill out this field');
        } else {
            // handle search here
            setErrorMessage('');
            let formattedSearchTerm = search.split(' ').join('-');
            navigate(`/books-search/${formattedSearchTerm}`);
        }
    };

    // Handler for enter key press in search input
    const handleKeyPress = (event) => {
        if (event.key === 'Enter') {
            handleSearch();
        }
    };

    // Render the component
    return (
        <div className="h-screen min-h-full w-screen min-w-full overflow-x-hidden  bg-[#3a0d0d] text-[#fa3329]">
            <div className="w-full h-full font-Rubik">
                <div className='flex flex-grow flex-col font-Rubik'>
                <div className='mt-6 font-extralight ml-6 text-2xl text-[#fa3329]'><h1>Book Haven</h1></div>
                <hr className=" w-screen ml-12 border-[#fa3329] mt-2"/>
                <nav className='mt-6 ml-6 mb-6'>
                    <a className='mr-6 hover:opacity-50 transition-opacity duration-300' href='/books'>Home</a>
                    <button onClick={() => setClickedSearch(true)} className='mr-6 hover:opacity-50 transition-opacity duration-300'>Search</button>
                    { clickedSearch && <form className='pt-5' onSubmit={(e) => e.preventDefault()}>
                        <input 
                               type="text" required
                               placeholder="Search for books"
                               className='border-b-2 border-b-[#b8413a] bg-transparent outline-none rounded-md p-1 mr-4'
                               value={search}
                               onChange={handleSearchChange}
                               onKeyPress={handleKeyPress}
                        />
                        <button className=' bg-gradient-to-tr from-[#fa3329] to-[#8d2626] text-[#3a0d0d] hover:bg-gradient-to-tr hover:from-[#8d2626] hover:to-[#fa3329] hover:opacity-50 hover:duration-300 py-2 px-4 rounded-xl' onClick={handleSearch} onSubmit={handleSearch}>Search</button>
                    </form> }
                </nav>
            </div>
                <div className='mb-8 mx-4 flex flex-wrap items-center justify-center'>
                    <GetBooks query={query} />
                </div>
            </div>
        </div>
    );
};

export default BooksSearched;