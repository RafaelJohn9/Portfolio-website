import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom';
import FrontBooksImage from '../imgs/Books.jpg'
import MysteryThriller from '../imgs/mystery_thriller.jpg'
import Romance from '../imgs/romance.jpg'
import SciFi from '../imgs/scifi.jpg'
import SelfHelp from '../imgs/selfhelp.jpg'
import Book from '../imgs/BackgroundBooks.2.jpg'

const Books = () =>{
    const [clickedSearch, setClickedSearch] = useState(false);
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
        <div className='h-screen w-screen flex font-Rubik flex-col flex-grow bg-[#3a0d0d] overflow-x-hidden text-[#fa3329]'>
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
            <div className='h-5/6 flex flex-col flex-grow gap-1'>  
                <div className='relative w-screen'>
                    <img src={FrontBooksImage} className='h-full w-screen' alt="" />
                    <div className='absolute inset-0 flex flex-col text-red-500 font-bold justify-center items-center'>
                        <div className='mx-24 md:mx-96'>
                            <h1 className="text-2xl md:text-5xl bg-gradient-to-r from-[#fa3329] to-blue-900 text-transparent bg-clip-text">Welcome!</h1>
                            <p className='font-semibold italic font-Rubik md:text-2xl bg-gradient-to-r from-[#fa3329] to-[#3a0d0d] text-transparent bg-clip-text'>Bookhaven, your ultimate destination for discovering and downloading captivating books!</p>
                        </div>
                    </div>
                </div>

                <div className='flex pt-4 flex-row flex-wrap justify-center items-center'>
                    <div className='flex flex-col justify-center items-center'>
                        <h1 className='font-Rubik font-semibold text-center text-2xl'>Featured Books</h1>
                        <hr className=" w-screen border-[#fa3329] mt-2"/>
                    </div>
                      <div className='grid grid-cols-1 md:grid-cols-2  gap-4'>
                        <div className='flex flex-col mt-4 hover:opacity-50 hover:duration-300 cursor-pointer'>
                            <a href='/books-search/mystery-thriller'>
                                <img src={MysteryThriller} className='justify-center items-center rounded-full md:w-4/5' alt="" />
                                <p className='mt-2 pl-24 lg:pl-56'>Mystery Thrillers, Collection</p>
                            </a>
                        </div>
                        <div className='flex flex-col hover:opacity-50 hover:duration-300 cursor-pointer'>
                            <a href='/books-search/romance'>
                                <img src={Romance} className='mt-4 rounded-full md:w-4/5' alt="" />
                                <p className='mt-2 pl-24 lg:pl-56'>Heartwarming Romance Collection</p>
                            </a>
                        </div>
                        <div className='flex flex-col hover:opacity-50 hover:duration-300 cursor-pointer'>
                            <a href='/books-search/scifi'>
                                <img src={SciFi} className='justify-center items-center rounded-full md:w-4/5' alt="" />
                                <p className='mt-2 pl-32 lg:pl-56'>Sci-fi extravaganza</p>
                            </a>
                        </div>
                        <div className='flex flex-col hover:opacity-50 hover:duration-300 cursor-pointer'>
                            <a href='/books-search/selfhelp'>
                                <img src={SelfHelp} className='justify-center items-center rounded-full md:w-4/5' alt="" />
                                <p className='mt-2  pl-28 lg:pl-56'>Top to Self-Help Books</p>
                            </a>
                        </div>
                      </div>
                </div>
                <hr className=" w-screen border-[#fa3329] mt-2"/>
                <div>
                    <h1 className='text-3xl pl-12 md:pl-24 font:bold'>Our Services</h1>
                    <hr className=" w-screen border-[#fa3329] mt-2"/>

                    <div className='flex flex-wrap'>
                        <img src={Book} alt="" className='ml-12 md:ml-24 mt-4 rounded-t-full w-3/5 md:w-1/5'/>
                        <div className='p-6 md:w-3/5 md:pl-10'>
                            <h1 className='font-semibold text-2xl'>Library Building</h1>
                            <br />
                            <h2 className='text-lg'>Fill your shelves</h2>
                            <br />
                            <p className=' text-md font-light'>We take pride in helping our clients build unique and personalized brand collections.
                                Our goal is to help you tell a story through the books you own, and we make sure every
                                book in that collection is part of that story.
                                At our core, 
                                we understand that each book holds within its pages a world of possibilities 
                                and a narrative waiting to be discovered. 
                                That's why we meticulously curate collections tailored to your tastes, 
                                ensuring that every addition resonates with your unique journey. 

                            </p>
                        </div>
                    </div>
                </div>
                <hr className=" w-screen border-[#fa3329] mt-2"/>
                <div className=''>
                    <h1 className='text-center font-bold text-2xl pt-4'>Book Haven</h1>
                    <h2 className='pt-10 px-8 text-xl font-semibold text-center'>Contact Info</h2>
                    <ul className='py-4 px-12  text-center flex flex-wrap gap-4 flex-col'>
                        <li>www.johnmkagunda.me</li>
                        <li>johnmkagunda@gmail.com</li>
                        <li>+254743153583</li>
                    </ul>
                    <div className='text-center bg-[#2c0c09] flex flex-col flex-wrap h-4/6 w-4/5  rounded-full mx-auto mt-5'>
                        <h3 className='text-center px-20 pt-20 pb-10 font-bold text-2xl font-Rubik'>Stay Informed- Join our Newsletter</h3>
                        <form className='flex flex-col items-center justify-center'>
                            <input className="mb-4  border-b-2 border-b-[#fa3329] bg-transparent  text-red-500 focus:outline-none text-center" type="text" placeholder="Enter your email here *"/>
                            <button className=' w-auto hover:opacity-50  hover:duration-500 text-center h-auto border-2 border-[#fe3430] py-2 px-6 rounded-sm  '>Submit</button>

                        </form>
                        <p className='text-center pt-4 text-xl font-thin'>Thank you for subscribing!</p>
                    </div>
                </div>
            </div>
        </div>
    );
}
export default Books;