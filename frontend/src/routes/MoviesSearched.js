/**
 * display page for searched movies
 */
import React from 'react';
import NavBar from '../components/CommonComponents/NavBar';
import moviesSearch from '../middleware/movies';
import { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import recommend from '../middleware/recommend';

const GetMovies = ({ query }) => {
    const [loading, setLoading] = useState(true);
    const [movies, setMovies] = useState([]);
    const [error, setError] = useState(null);


    useEffect(() => {
        const fetchMovies = async () => {
            setLoading(true);
            try {
                const data = await moviesSearch(query);
                setMovies(data);
            } catch (error) {
                setError(error.message);
            }
            setLoading(false);
        };

        fetchMovies();
    }, [query]);

    if (error) {
        return <div>Error: {error}</div>;
    }

    if (loading) {
        return <div>Loading...</div>;
    }

    if (!query) {
        return null;
    }


    return (
        <div className='pl-10 h-full w-full text-white italic font-custom flex flex-wrap gap-32'>
            {console.log(movies)}
            {movies.length === 0 ? (
                <h1 className='text-4xl'>No results found</h1>
            ) : (
                movies.map((movie, index) => {
                    if (!movie.poster || movie.poster === 'N/A') {
                        return null;
                    }
                    return (
                        <div key={index} className='bg-grey-500 h-64 w-60 mb-48 md:ml-0 sm:ml-16 mt-16 relative group'>
                            <div className='h-1/2'></div>
                            <img src={movie.poster} alt="" />
                            <h1 className='text-center font-extrabold'>Title: {movie.title}</h1>
                            <p className='text-center'>Release Date: {movie.release_date}</p>
                            <h2 className='font-bold text-lg text-green-500 text-center'>Rating:</h2>
                            <p className='text-center pl-32 text-red-200'>{movie.rating}/10</p>
                            <button className='ml-6 bg-red-600 font-custom hover:bg-red-800 rounded-full mt-5 text-black w-4/5' onClick={async (event) => {
                                    event.target.innerText = 'Recommended';
                                    await recommend(movie);
                            }}>Recommend</button>
                        </div>
                    );
                })
            )}
        </div>
    );
};

const MoviesSearched = () => {
    const location = useLocation();
    const query = location.pathname.split('/')[2].replace(/-/g, ' '); 
    console.log(query);
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
        <div className="h-screen min-h-full w-screen min-w-full overflow-x-hidden  bg-black">
            <NavBar />
            <div className="w-full h-full">
                <div className="flex rounded-lg border-0 md:w-1/2 sm:w-full pt-24 justify-center items-center">
                    <input
                        type="text" required
                        value={searchTerm}
                        onChange={handleSearchChange}
                        onKeyPress={handleKeyPress}
                        placeholder="Search for movies..."
                        className="w-full px-4 py-2 text-lg bg-gray-950 rounded-full outline-none hover:bg-grey-500 text-white"
                    />
                    <button onClick={handleSearch} className="px-4 py-2 bg-blue-950  text-white  rounded-full hover:bg-black">
                        Search
                    </button>
                    {errorMessage && <p className="text-red-500">{errorMessage}</p>}
                </div>
                <div className='grid grid-rows-4'>
                    <GetMovies query={query} />
                </div>
            </div>
        </div>
    );
};

export default MoviesSearched;