import React, { useState } from 'react';
import BackGroundMusicImage from '../imgs/BackGroundMusic.jpg'
import NavBar from '../components/CommonComponents/NavBar';
import { useNavigate } from 'react-router-dom';


const MusicSearch = () => {
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
            navigate(`/music-search/${formattedSearchTerm}`);
        }
    };

    const handleKeyPress = (event) => {
        if (event.key === 'Enter') {
            handleSearch();
        }
    };

    return (
        <div className="min-h-screen flex items-center justify-center bg-cover bg-center" style={{ backgroundImage: `url(${BackGroundMusicImage})` }}>
            <NavBar />
            <div className="flex mt-52 md:mt-64 rounded-lg border-0 md:w-1/2 sm:w-full lg:mt-96">
                <input
                    type="text" required
                    value={search}
                    onChange={handleSearchChange}
                    onKeyPress={handleKeyPress}
                    placeholder="Search Music"
                    className="w-full px-4 py-2 text-lg  rounded-full outline-none bg-gray-800 text-white"
                />
                <button onClick={handleSearch} className="px-4 py-2 hover:bg-gray-950  text-white  rounded-full bg-gray-800">
                    Search
                </button>
                {errorMessage && <p className="text-red-500">{errorMessage}</p>}
            </div>
        </div>
    );
};

export default MusicSearch;