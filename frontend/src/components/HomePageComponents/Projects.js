import React from 'react';
import ShellDisplay from '../HomePageComponents/projects/shell_project'

const Projects = () => {
    return (
        <div className="flex flex-col flex-grow center justify-center">
            <h1 className=' text-4xl text-center font-extrabold'>Real World Projects and Experiences</h1>
            <ShellDisplay />
        </div>
    );
}

export default Projects;