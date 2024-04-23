import React from 'react';
import ShellImage from '../../../imgs/shell.png';

const ShellDisplay = () => {
    return (
        <div className="flex justify-center flex-wrap mt-4 flex-grow overflow-y-auto">
            <h1 className="text-xl font-extrabold">1)  Simple Shell</h1>
            <div className='flex md:m-10 mx-4 flex-wrap md:flex-nowrap'>
                   <img src={ShellImage} alt="shell" className="rounded-3xl" />
                <div className="flex  md:my-0 my-4 flex-col  bg-gradient-to-tr md:mx-5 from-green-700 to-gray-600 rounded-3xl italic flex-grow hover:from-gray-600 hover:to-green-700">
                    <p className="sm:text-sm md:text-lg mx-10 my-4 px-4  font-sans font-semibold">A fully functional shell implementation crafted in C programming language.</p> 
                    <p className='px-8'>
                    <br />
                    My motivation behind developing this shell project stemmed from a desire to deepen my understanding 
                    of system-level programming and enhance my proficiency in C. 
                    As a fundamental component of operating systems, 
                    shells fascinated me with their ability to interpret user commands and interact with the underlying system. 
                    By embarking on this project, I sought to not only reinforce my programming skills 
                    but also gain practical experience in handling processes, managing input/output streams, 
                    and implementing complex functionalities like piping and redirection. Through this endeavor, 
                    I aimed to challenge myself, broaden my knowledge, 
                    and ultimately contribute to my growth as a software developer.
                     </p>
                     <div className='mx-4 flex items-center justify-center gap-12 mt-5 flex-wrap mb-4 font-semibold'>
                     <button onClick={() => window.open('/shell', '_blank')} className='bg-gradient-to-tr from-gray-500 to-green-900 h-24 rounded-full w-48 hover:from-green-900 hover:to-gray-500'>See demo
                        <br/>(Dockerised)
                     </button>
                     <button  onClick={() => window.open('https://github.com/RafaelJohn9/simple_shell', '_blank')} className='bg-gradient-to-tr from-gray-500 to-green-900 h-24 w-48 hover:from-green-900 hover:to-gray-500 flex rounded-full justify-center items-center flex-col'>
                        See Source code
                        <img width="50" height="50" src="https://img.icons8.com/ios-filled/50/github.png" alt="github"></img>
                    </button>
                     </div>
                </div>

            </div>
        </div>
    );
};

export default ShellDisplay;