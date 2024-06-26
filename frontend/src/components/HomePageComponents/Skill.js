import React from 'react';
import getSkills from '../../middleware/skills';
import './Skills.css';
import InfiniteHorizontalScroll from './InfiniteHorizontalScroll'

const SkillsJson = await getSkills() || [];


const Skill = (skill) => {
    return (
    <a href={skill.direct_link } target='_blank' rel='noreferrer'>
        <div className="w-64 h-4/5  mx-11 animate-scroll">
            <img src={`data:image/svg+xml;utf8,${encodeURIComponent(skill.images.xl)}`} alt="" />
            <p className='text-center'>{skill.name}</p>
        </div>
    </a> 
    );
};

const Skills = () => {
        return (
            <div className='overflow-x-auto  h-full w-full overflow-auto'>
                <h1 className='text-4xl text-center font-extrabold'>My WebStack</h1>
                <p className='text-center text-lg italic'>Click on a skill to see related projects in GitHub</p>
                <div className='overflow-x-auto flex h-full w-full overflow-auto'>
                    <InfiniteHorizontalScroll>
                        {
                        SkillsJson.map((skill, index) => (
                        <Skill {...skill} key={index} />
                        ))
                        }
                    </InfiniteHorizontalScroll>
            </div>
            </div>
        );
};

export default Skills;
