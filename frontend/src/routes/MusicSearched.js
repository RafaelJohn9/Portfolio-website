/**
 * display page for searched music
 */
import NavBar from '../components/CommonComponents/NavBar';
import musicSearch from '../middleware/music';
import { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import { motion } from "framer-motion";
import recommend from '../middleware/recommend';


const GetMusic = ({ query }) => {
    const [music, setMusic] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchMusic = async () => {
            try {
                const data = await musicSearch(query);
                setMusic(data);
            } catch (error) {
                setError(error.message);
            }
        };

        fetchMusic();
    }, [query]);

    const [show, setShow] = useState(false);

    useEffect(() => {
        const timer = setTimeout(() => {
            setShow(true);
        }, 5000);
        return () => clearTimeout(timer);
    }, [error]);

    const [playingIndex, setPlayingIndex] = useState(null); // Track index of currently playing track

    return show ? (
        <div className='pl-10 h-full w-full text-white italic font-custom flex flex-wrap gap-32'>
            {music.length === 0 ? (
                <h1 className='text-4xl'>No results found</h1>
            ) : (
                music.map((track, index) => {
                    if (!track['Album Artwork']) {
                        return null;
                    }
                    return (
                        <div key={index} className='bg-grey-500 h-64 w-60 mb-48 md:ml-0 sm:ml-16 mt-16 relative group'>
                            <div className='h-1/2'></div>
                            <img src={track['Album Artwork']} alt="" />

                            <div>
                                <h1 className='text-center font-extrabold'>Title: {track['Track Name']}</h1>
                                {track['Preview URL or Track URI'].startsWith('https') ? (
                                    <div>
                                        {playingIndex === index ? (
                                            <button onClick={() => setPlayingIndex(null)}><img width="100" height="100" src="https://img.icons8.com/ios/100/pause--v1.png" alt="Pause"/></button>
                                        ) : (
                                            <button onClick={() => setPlayingIndex(index)}><img width="100" height="100" src="https://img.icons8.com/ios-filled/100/circled-play.png" alt="Play"/></button>
                                        )}
                                        {playingIndex === index && 
                                            <iframe 
                                                     src={track['Preview URL or Track URI']} 
                                                     title="Music Track" 
                                                     width="300" height="100" 
                                                     frameborder="0" 
                                                     allowtransparency="true" 
                                                     autoplay="false"></iframe>
                                        }
                                    </div>
                                ) : null}
                            </div>
                            <p className='text-center'>Artist: {track['Artist(s) Name']}</p>
                            <p className='text-center'>Release Date: {track['release_date']}</p>
                            <button className='ml-6 bg-red-600 font-custom hover:bg-red-800 rounded-full mt-5 text-black w-4/5' onClick={async (event) => {
                                    event.target.innerText = 'Recommended';
                                    await recommend(music);
                            }}>Recommend</button>
                            <a href={track['Direct Link']} target='_blank' rel='noreferrer' className="font-extrabold text-red-400">Song Direct Link</a>
                        </div>
                    );
                })
            )}
        </div>
    ) : null;
};

const MusicSearched = () => {
    const location = useLocation();
    const navigate = useNavigate();

    const query = location.pathname.split('/')[2].replace(/-/g, ' '); 
    console.log(query);
    const [searchTerm, setSearchTerm] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

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
            navigate(`/music-search/${formattedSearchTerm}`);
        }
    };

    const handleKeyPress = (event) => {
        if (event.key === 'Enter') {
            handleSearch();
        }
    };
    return (
        <div className="min-h-screen h-screen w-screen  min-w-screen overflow-x-hidden bg-gradient-to-tr from-blue-950 to-[#000000]">
            <NavBar />
            <div>
        <motion.div className="absolute w-40 h-40 bg-green-900 rounded-full animate-pulse opacity-20 blur-lg" 
        animate={{ scale: [0.9, 1.1], opacity: [0.1, 0.6] }} 
        transition={{ duration: 2, repeat: Infinity, repeatType: "reverse" }} 
      />
      <motion.div className="absolute w-32 h-32 bg-green-900 rounded-full animate-pulse opacity-20 blur-lg" 
        style={{ top: "30%", left: "20%" }} 
        animate={{ scale: [0.8, 1.2], opacity: [0.1, 0.6] }} 
        transition={{ duration: 3, repeat: Infinity, repeatType: "reverse" }} 
      />
      <motion.div className="absolute w-24 h-24 bg-green-900 rounded-full animate-pulse opacity-20 blur-lg" 
        style={{ bottom: "20%", right: "15%" }} 
        animate={{ scale: [0.7, 1.3], opacity: [0.1, 0.6] }} 
        transition={{ duration: 4, repeat: Infinity, repeatType: "reverse" }} 
      />
      <motion.div className="absolute w-20 h-20 bg-green-900 rounded-full animate-pulse opacity-20 blur-lg" 
        style={{ top: "40%", right: "10%" }} 
        animate={{ scale: [0.6, 1.4], opacity: [0.1, 0.6] }} 
        transition={{ duration: 5, repeat: Infinity, repeatType: "reverse" }} 
      />
      <motion.div className="absolute w-20 h-20 bg-green-900 rounded-full animate-pulse opacity-20 blur-lg" 
        style={{ top: "70%", right: "50%" }} 
        animate={{ scale: [0.9, 1.4], opacity: [0.1, 0.6] }} 
        transition={{ duration: 5, repeat: Infinity, repeatType: "reverse" }} 
      />
      <motion.div className="absolute w-20 h-20 bg-green-900 rounded-full animate-pulse opacity-20 blur-lg" 
        style={{ top: "70%", left: "10%" }} 
        animate={{ scale: [3.6, 2.4], opacity: [0.1, 0.6] }} 
        transition={{ duration: 5, repeat: Infinity, repeatType: "reverse" }} 
      />
        <motion.div className="absolute w-20 h-20 bg-green-900 rounded-full animate-pulse opacity-20 blur-lg" 
        style={{ top: "40%", right: "50%" }} 
        animate={{ scale: [3.6, 2.4], opacity: [0.1, 0.6] }} 
        transition={{ duration: 5, repeat: Infinity, repeatType: "reverse" }} 
      /></div>
            <div className="w-full h-full">
                <div className="flex rounded-lg border-0 md:w-1/2 sm:w-full pt-24 justify-center items-center">
                    <input
                        type="text" required
                        value={searchTerm}
                        onChange={handleSearchChange}
                        onKeyPress={handleKeyPress}
                        placeholder="Search for music..."
                        className="w-full  px-4 py-2 text-lg rounded-full outline-none bg-[#0c0202] text-white"
                    />
                    <button onClick={handleSearch} className="px-4 py-2 bg-[#0c0202]  text-white  rounded-full hover:bg-gray-500">
                        Search
                    </button>
                    {errorMessage && <p className="text-red-500">{errorMessage}</p>}
                </div>
                <div className='grid grid-rows-4'>
                    <GetMusic query={query} />
                </div>
            </div>
        </div>
    );
};

export default MusicSearched;
