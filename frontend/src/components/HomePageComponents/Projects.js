import React from 'react';
import ShellDisplay from '../HomePageComponents/projects/shell_project'
import TravelKenyaDisplay from '../HomePageComponents/projects/travekenya_project'

const Projects = () => {
    return (
        <div className="flex flex-col flex-grow center justify-center mt-12">
            <h1 className=' text-4xl text-center font-extrabold'>Real World Projects and Experiences</h1>
            <ShellDisplay />
            <TravelKenyaDisplay />
        </div>
    );
}

export default Projects;