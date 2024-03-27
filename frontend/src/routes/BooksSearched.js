import React, { useState, useEffect } from 'react';
import NavBar from '../components/CommonComponents/NavBar';
import booksSearch from '../middleware/books';
import { useLocation, useNavigate } from 'react-router-dom';

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
        <div className='pl-10 h-full w-full text-black italic font-custom flex flex-wrap gap-32'>
            {books.length === 0 ? (
                <h1 className='text-4xl'>No results found</h1>
            ) : (
                books.map((book, index) => {
                    if (!book.cover_images || book.cover_images.thumbnail === 'N/A') {
                        return null;
                    }
                    return (
                        <div key={index} className='bg-grey-950 h-64 w-60 mb-48 md:ml-0 sm:ml-16 mt-16 relative group'>
                            <div className='h-1/2'></div>
                            <img src={book.cover_images.thumbnail} alt="" />
                            <h1 className='text-center font-extrabold'>Title: {book.title}</h1>
                            <p className='text-center'>Release Date: {book.release_date}</p>
                            {book.rating && (
                                <div>
                                    <h2 className='font-bold text-lg text-green-500 text-center'>Rating:</h2>
                                    <p className='text-center pl-32 text-red-500 font-bold'>{book.rating} /10</p>
                                </div>
                            )}
                            <button className='ml-6 bg-red-600 font-custom hover:bg-red-800 rounded-full mt-5 text-black w-4/5'>Recommend</button>
                        </div>
                    );
                })
            )}
        </div>
    );
};

// Main component for searching books
const BooksSearched = () => {
    // Hooks for location and navigation
    const location = useLocation();
    const navigate = useNavigate();

    // Extracting search query from the URL
    const query = location.pathname.split('/')[2].replace(/-/g, ' '); 

    // State variables for search term and error message
    const [searchTerm, setSearchTerm] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    // Handler for search input change
    const handleSearchChange = (event) => {
        setSearchTerm(event.target.value);
    };

    // Handler for search action
    const handleSearch = () => {
        if (searchTerm === '') {
            setErrorMessage('Please fill out this field');
        } else {
            setErrorMessage('');
            let formattedSearchTerm = searchTerm.split(' ').join('-');
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
        <div className="h-screen min-h-full w-screen min-w-full overflow-x-hidden  bg-gray-300 text-black">
            <NavBar />
            <div className="w-full h-full">
                <div className="flex rounded-lg border-0 md:w-1/2 sm:w-full pt-24 justify-center items-center">
                    <input
                        type="text" required
                        value={searchTerm}
                        onChange={handleSearchChange}
                        onKeyPress={handleKeyPress}
                        placeholder="Search for books..."
                        className="w-full px-4 py-2 text-lg bg-gray-400 rounded-full outline-none hover:bg-grey-500 text-black"
                    />
                    <button onClick={handleSearch} className="px-4 py-2 bg-blue-950  text-white  rounded-full hover:bg-black">
                        Search
                    </button>
                    {errorMessage && <p className="text-red-500">{errorMessage}</p>}
                </div>
                <div className='grid grid-rows-4'>
                    <GetBooks query={query} />
                </div>
            </div>
        </div>
    );
};

export default BooksSearched;