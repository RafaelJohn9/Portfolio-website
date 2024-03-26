import React from 'react';
import { motion, useAnimation } from 'framer-motion';
import { useInView } from 'react-intersection-observer';
import { useEffect } from 'react';

const About = () => {
    const controls = useAnimation();
    const { ref, inView } = useInView({
        threshold: 0.1,
    });

    useEffect(() => {
        if (inView) {
            controls.start({
                scale: 1,
                transition: { duration: 0.5 }
            });
        }
        if (!inView) {
            controls.start({ scale: 0.8 });
        }
    }, [controls, inView]);

    return (
        <motion.div 
            ref={ref}
            animate={controls}
            className="h-full w-full flex items-center justify-center"
            initial={{ scale: 0.7 }}
        >
            <div className="lg:px-64 font-custom">
                <h1 className='text-center font-extrabold text-lg sm:text-lg md:text-xl lg:text-2xl xl:text-3xl'>About me</h1>
                <p className="text-center font-sans text-lg sm:text-lg md:text-xl lg:text-xl xl:text-xl">
                I am John M Kagunda, 
                I am a junior fullstack developer fueled by a passion for crafting innovative solutions in the digital realm. 
                With a keen eye for detail and a thirst for knowledge, 
                I dive into the intricacies of both front-end and back-end development, 
                striving for seamless user experiences and robust functionality. 
                Equipped with a foundation in coding languages and frameworks, 
                I am dedicated to honing my skills and staying abreast of emerging technologies to create impactful applications. 
                My commitment to continuous learning and problem-solving propels me forward on my journey to becoming a proficient 
                and versatile developer in the ever-evolving landscape of technology.
                </p>
            </div>
        </motion.div>
    );
}

export default About;

