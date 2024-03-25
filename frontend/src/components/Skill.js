import React from 'react';
import getSkills from '../middleware/skills';

const SkillsJson = getSkills();


const Skill = (skill) => {
    return (
        <div className="skill">
            <image src={skill.images} alt={skill.name} />
        </div>
    );
};

const Skills = () => {
    return (
        <div>
           {
             SkillsJson.map((skill, index) => (
                Skill({...skill, key: index})
                ))
           }
        </div>
    );
};

export default Skills;