import React from 'react';
import travelKenyaImage from '../../../imgs/travelKenya.png';

const TravelKenyaDisplay = () => {
    return (
        <div className="flex justify-center flex-wrap flex-grow overflow-y-auto mt-24">
            <h1 className="text-xl font-extrabold">2) TravelKenya</h1>
            <div className='flex md:m-10 mx-4 flex-wrap md:flex-nowrap mt-5'>
                <img src={travelKenyaImage} alt="travelKenya" className="rounded-3xl" />
                <div className="flex  md:my-0 my-4 flex-col  bg-gradient-to-tr md:mx-5 from-green-700 to-gray-600 rounded-3xl italic flex-grow hover:from-gray-600 hover:to-green-700">
                    <p className="sm:text-sm md:text-lg mx-10 my-4 px-4  font-sans font-semibold justify-center flex">TravelKenya</p> 
                    <p className='px-8'>
                    <br />
                    TravelKenya is an interesting online platform crafted with the MERN stack, 
                    inviting adventurers to explore the breathtaking landscapes and vibrant cultures of Kenya. 
                    From the bustling streets of Nairobi to the serene savannas of the Maasai Mara, 
                    this site seamlessly integrates MongoDB, Express.js, React, and Node.js to deliver a dynamic user experience. 
                    With its sleek design and intuitive interface, travelers can easily browse through a myriad of destinations, 
                    discover hidden gems, and plan their dream safari or coastal getaway. 
                    Whether seeking adrenaline-pumping adventures or tranquil retreats, 
                    TravelKenya offers a gateway to unforgettable experiences in the heart of East Africa.
                    <br/>
                    <br/>
                    (Collaborated with <a href='https://github.com/kaleabendrias' className='text-gray-400' target='blank'rel='noreferrer'>Kaleab Endrias</a>)
                    <br/>
                    My role: Backend developer 
                     </p>
                     <div className='mx-4 flex items-center justify-center gap-12 mt-5 flex-wrap mb-4 font-semibold'>
                     <a className='bg-gradient-to-tr from-gray-500 to-green-900 h-24 rounded-full w-48 hover:from-green-900 hover:to-gray-500 flex items-center justify-center' href='https://travel-kenya-mauve.vercel.app/' target='blank' rel='noreferrer'>
                        See Site ↗
                     </a>
                     <a  href='https://github.com/kaleabendrias/travel_kenya' target='blank' className='bg-gradient-to-tr from-gray-500 to-green-900 h-24 w-48 hover:from-green-900 hover:to-gray-500 flex rounded-full justify-center items-center flex-col' rel='noreferrer'>
                        See Source code
                        <img width="50" height="50" src="https://img.icons8.com/ios-filled/50/github.png" alt="github"></img>
                    </a>
                     </div>
                </div>

            </div>
        </div>
    );
};

export default TravelKenyaDisplay;