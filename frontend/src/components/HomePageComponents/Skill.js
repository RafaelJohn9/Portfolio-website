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
            <div className='overflow-x-auto flex h-full w-full'>
                <InfiniteHorizontalScroll>
                    {
                    SkillsJson.map((skill, index) => (
                        <Skill {...skill} key={index} />
                        ))
                    }
                </InfiniteHorizontalScroll>
            </div>
        );
};

export default Skills;
