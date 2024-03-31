import React, { useState } from 'react';
import NavBar from '../components/CommonComponents/NavBar';
import BackGroundMoviesImage from '../imgs/BackgroundMovies.jpg'
import { useNavigate } from 'react-router-dom';




const MoviesSearch = () => {
    const [searchTerm, setSearchTerm] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const navigate = useNavigate();

    const handleSearchChange = (event) => {
        setSearchTerm(event.target.value);
    };

    const handleSearch = () => {
        if (searchTerm === '') {
            setErrorMessage('Please fill out this field');
        } else {
            // handle search here
            setErrorMessage('');
            let formattedSearchTerm = searchTerm.split(' ').join('-');
            navigate(`/movies-search/${formattedSearchTerm}`);
        }
    };

    const handleKeyPress = (event) => {
        if (event.key === 'Enter') {
            handleSearch();
        }
    };

    return (
        <div  className="relative flex items-center justify-center h-screen md:bg-cover md:bg-center bg-black" style={{backgroundImage: `url(${BackGroundMoviesImage})`, backgroundPosition: 'center'}}>

            <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDU4MnlpdGFpZG1tcjg1bWc0cHhlb2Fieml2amFqanU5bGJoZnJrcyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/d2Z6aAm3Z2GdLrHi/200.webp" alt="" className="absolute top-0 left-0 z-0" />
            <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDU4MnlpdGFpZG1tcjg1bWc0cHhlb2Fieml2amFqanU5bGJoZnJrcyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/d2Z6aAm3Z2GdLrHi/200.webp" alt="" className="absolute top-0 right-0 z-0" />
            <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDU4MnlpdGFpZG1tcjg1bWc0cHhlb2Fieml2amFqanU5bGJoZnJrcyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/d2Z6aAm3Z2GdLrHi/200.webp" alt="" className="absolute bottom-0 right-0 z-0" />
            <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDU4MnlpdGFpZG1tcjg1bWc0cHhlb2Fieml2amFqanU5bGJoZnJrcyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/d2Z6aAm3Z2GdLrHi/200.webp" alt="" className="absolute bottom-0 left-0 z-0" />
            <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDU4MnlpdGFpZG1tcjg1bWc0cHhlb2Fieml2amFqanU5bGJoZnJrcyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/d2Z6aAm3Z2GdLrHi/200.webp" alt="" className="absolute bottom-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 z-0" />
            <NavBar />
            <div className="flex mt-32 md:mt-64 rounded-lg border-0 md:w-1/2 sm:w-full lg:mt-96">
                <input
                    type="text" required
                    value={searchTerm}
                    onChange={handleSearchChange}
                    onKeyPress={handleKeyPress}
                    placeholder="Search for movies..."
                    className="w-full px-4 py-2 text-lg bg-black rounded-full outline-none hover:bg-grey-500 text-white"
                />
                <button onClick={handleSearch} className="px-4 py-2 hover:bg-blue-950  text-white  rounded-full bg-black">
                    Search
                </button>
                {errorMessage && <p className="text-red-500">{errorMessage}</p>}
            </div>
        </div>
    );
};

export default MoviesSearch;
