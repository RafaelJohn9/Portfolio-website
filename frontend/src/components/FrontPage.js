import React from "react";
import './FrontPage.css';
import ProfileImage from '../imgs/official_image_2.png';

    const FrontPage = () => {
        return (
            <div className="relative overflow-hidden flex flex-grow-0">
                <div className="w-1/2 opacity-0 animate-fade-in  text-[#77adff]">
                    <h1 className="text-center text-xl sm:text-2xl md:text-3xl lg:text-4xl xl:text-5xl font-serif italic">Welcome to my portfolio website</h1>
                    <h2>John Mwangi Kagunda</h2>
                    <h3>A Junior FullStack Developer</h3>
                </div>
                
                <div className="flex items-center flex-grow h-3/5 w-1/2 justify-center mr-0 pr-0">
                    <img src={ProfileImage} alt="Profile" className="md:h-2/5 w-4/5"/>
                </div>
            </div>
        );
    };


export default FrontPage;
