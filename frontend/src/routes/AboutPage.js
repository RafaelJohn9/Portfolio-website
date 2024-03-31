import ProfilePhoto from '../imgs/official_image_2.jpg'
import React from 'react';
import NavBar from '../components/CommonComponents/NavBar';

const AboutPage = () => {
    return (
        <div className="flex flex-col items-center justify-center min-h-screen py-2 bg-gradient-to-tr from-green-900 to-green-100">
            <NavBar />
            <img src={ProfilePhoto} alt="Profile" className="rounded-full h-64 w-64 md:h-96 md:w-96 mt-48" />
            <h1 className="mt-6 text-2xl font-semibold text-black  font-custom">John Kagunda</h1>
            <h2 className="mt-2 text-lg text-black font-medium">FullStack Software Developer</h2>
            <h3>FAQs</h3>
            <div>
                <h4 className='font-extrabold'>What is your favorite programming language and why?</h4>
                <p className='italic pl-10'>Python, It was my first programming language😅</p>
                <br />
                <h4 className='font-extrabold'>How did you acquire your skills?</h4>
                <p className='italic pl-10'>
                    I acquired most of my skills in a 12-month Software Engineering Program in  
                    <a href='https://www.alxafrica.com' target='_blank' rel="noreferrer" className='text-red-800'>  alxafrica </a>
                    which is in association with Holberton School of Technology
                </p>
                <br />
                <h4 className='font-extrabold'>What projects have you worked on?</h4>
                <p className='italic pl-10'>
                    alxafrica software engineering program focus on impacting skills to their students 
                    using real life challenges facing the tech industry as projects 
                    and also teaches right pratices used in the current tech industry.
                    <br />
                    Some of the projects include:
                    <br />
                    <ul className='pl-10 list-disc'> 
                        <li>Version Control - understanding what is git and going to indepth on how to use version control. </li>
                        <li>CommandLine Interface (CLI) - understanding linux file system structure, Introduction to Bash CLI, bash scripting and deep dive of efficiently using the CLI.</li>
                        <li>C programming language - Learning the syntax of C Programming language, the industry standards in terms of programmming patterns, styles and others</li>
                        <li>Algorithm and DataStructures - The different Data Structures their strengths and weaknesses different optimized algorithms in solving common problems such as Search algorithms, Sort algorithms and others</li>
                        <li>Backend development - Working with backend technologies to achieve s database management, implementing security measures, optimizing caching systems, 
                            and designing efficient algorithms to ensure the reliability, 
                            scalability, and performance of web applications. </li>
                        <li>Server Configuration - Configuring a remote server only using an SSH connection, Writing automation scripts using bash and puppet scripting languages also web server configuration</li>
                        <li>Frontend development - Working with frontend technologies such as HTML, CSS, JavaScript, ReactJs, TailwindCSS</li>
                    </ul>
                </p>
                <br />
                <h4 className='font-extrabold'>What is your approach to problem-solving?</h4>
                <p className='italic pl-10'>
                    I usually start by understanding the problem thoroughly,
                    then I break it down into smaller, 
                    manageable tasks. I then solve each task one at a time.
                </p>
                <br />
                <h4 className='font-extrabold'>What is Backend development and why did you decide of  to major in it?</h4>
                <p className='italic pl-10'>
                Backend development involves the creation and maintenance of the server-side logic,
                 databases, and APIs that power web applications.
                  It's essentially the "behind-the-scenes" work that makes a website or web application function properly.
                 Backend developers handle tasks such as server management, database integration, 
                 business logic implementation, security, and scalability.
                 </p>
                 <br/>
                <p className='italic pl-10'>
                 As for why I decided to major in it is due to
                 Interest in problem-solving: 
                 Backend development often involves complex problems related to data processing,
                system architecture, and performance optimization.
                 For individuals like me who enjoy solving puzzles and tackling challenges, 
                 backend development can be intellectually stimulating.
                <a href='https://leetcode.com/RafaelJohn/' target='_blank' rel="noreferrer" className='text-red-800'>  You can check my LeetCode Profile </a>
                if you are a new developer and you need to  get yourself up to date on DSA. 
                I have some code posts on common DSA questions with optimized algorithms used to solve them.
                 </p>
                <br />
                <h4 className='font-extrabold'>What do you enjoy most about programming?</h4>
                <p className='italic pl-10'>
                    I enjoy the challenge of solving complex problems and the 
                    satisfaction of building something from scratch.
                </p>
                <br />
                <h4 className='font-extrabold'>Any advice for someone looking to get into software development?</h4>
                <p className='italic pl-10'>
                    Start by learning the basics of a programming language, 
                    then build small projects to apply what you've learned. 
                    Don't be afraid to ask for help and always keep learning.
                </p>
            </div>
        </div>
    );
}

export default AboutPage;