import React, { useState } from 'react';
import NavBar from '../components/CommonComponents/NavBar';
import BackGroundMoviesImage from '../imgs/BackgroundMovies.jpg'

const MoviesSearch = () => {
    const [searchTerm, setSearchTerm] = useState('');

    const handleSearchChange = (event) => {
        setSearchTerm(event.target.value);
    };

    return (
        <div className="flex items-center justify-center h-screen bg-cover" style={{backgroundImage: `url(${BackGroundMoviesImage})`}}>
            <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDU4MnlpdGFpZG1tcjg1bWc0cHhlb2Fieml2amFqanU5bGJoZnJrcyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/d2Z6aAm3Z2GdLrHi/200.webp" alt="" className="absolute top-0 left-0" />
            <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDU4MnlpdGFpZG1tcjg1bWc0cHhlb2Fieml2amFqanU5bGJoZnJrcyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/d2Z6aAm3Z2GdLrHi/200.webp" alt="" className="absolute top-0 right-0" />
            <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDU4MnlpdGFpZG1tcjg1bWc0cHhlb2Fieml2amFqanU5bGJoZnJrcyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/d2Z6aAm3Z2GdLrHi/200.webp" alt="" className="absolute bottom-0 right-0" />
            <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDU4MnlpdGFpZG1tcjg1bWc0cHhlb2Fieml2amFqanU5bGJoZnJrcyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/d2Z6aAm3Z2GdLrHi/200.webp" alt="" className="absolute bottom-0 left-0" />
            <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDU4MnlpdGFpZG1tcjg1bWc0cHhlb2Fieml2amFqanU5bGJoZnJrcyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/d2Z6aAm3Z2GdLrHi/200.webp" alt="" className="absolute bottom-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2" />
            <NavBar />
            <div className="flex border-2 rounded-lg border-black md:w-1/2 sm:w-full lg:mt-96">
                <input
                    type="text"
                    value={searchTerm}
                    onChange={handleSearchChange}
                    placeholder="Search for movies..."
                    className="w-full px-4 py-2 text-lg bg-black rounded-full outline-none hover:bg-grey-500 text-white"
                />
                <button className="px-4 py-2 hover:bg-blue-950  text-white  rounded-full bg-black">
                    Search
                </button>
            </div>
        </div>
    );
};

export default MoviesSearch;
