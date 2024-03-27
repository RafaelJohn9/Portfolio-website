import React, { useState } from 'react';
import BackgroundImage from '../imgs/BackGroundBooks.jpg'
import NavBar from '../components/CommonComponents/NavBar';
import { useNavigate } from 'react-router-dom';

const BookSearch = () => {
    const [search, setSearch] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const navigate = useNavigate();

    const handleSearchChange = (event) => {
        setSearch(event.target.value);
    };

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

    const handleKeyPress = (event) => {
        if (event.key === 'Enter') {
            handleSearch();
        }
    };

    return (
        <div className="min-h-screen flex items-center justify-center bg-cover bg-center" style={{ backgroundImage: `url(${BackgroundImage})` }}>
            <NavBar />
            <div className="flex justify-center items-center rounded-lg border-0 md:w-1/2 sm:w-full">
                <input
                    type="text" required
                    value={search}
                    onChange={handleSearchChange}
                    onKeyPress={handleKeyPress}
                    placeholder="Search Book"
                    className="w-full px-4 py-2 text-lg rounded-full outline-none bg-gray-800 text-white shadow-lg"
                />
                <button onClick={handleSearch} className="px-4 py-2 hover:bg-gray-950 text-white rounded-full bg-gray-800 shadow-lg transition duration-500 ease-in-out transform hover:-translate-y-1 hover:scale-110">
                    Search
                </button>
                {errorMessage && <p className="text-red-500">{errorMessage}</p>}
            </div>
        </div>
    );
};

export default BookSearch;