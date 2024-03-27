import React, { useState } from 'react';
import BackGroundMusicImage from '../imgs/BackGroundMusic.jpg'
import NavBar from '../components/CommonComponents/NavBar';


const MusicSearch = () => {
    const [search, setSearch] = useState('');

    const handleSearch = (event) => {
        event.preventDefault();
        // Handle your search logic here
        console.log(search);
    };

    return (
        <div className="min-h-screen flex items-center justify-center bg-cover bg-center" style={{ backgroundImage: `url(${BackGroundMusicImage})` }}>
            <NavBar />
            <form onSubmit={handleSearch} className="w-full max-w-sm">
                <div className="flex items-center border-b-2 border-teal-500 py-2">
                    <input
                        className="appearance-none bg-transparent border-none w-full text-black mr-3 py-1 px-2 leading-tight lg:text-2xl focus:outline-none"
                        type="text" required
                        placeholder="Search Music"
                        aria-label="Search Music"
                        value={search}
                        onChange={(e) => setSearch(e.target.value)}
                    />
                    <button
                        className="flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded"
                        type="submit"
                    >
                        Search
                    </button>
                </div>
            </form>
        </div>
    );
};

export default MusicSearch;