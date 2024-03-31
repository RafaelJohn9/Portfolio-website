import React from 'react';
import { motion, useAnimation } from 'framer-motion';
import { useInView } from 'react-intersection-observer';
import { useEffect } from 'react';
import { Link } from 'react-router-dom';

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
                I'm John M Kagunda, 
                a Junior FullStack Developer specializing in backend technologies. 
                I'm passionate about creating innovative solutions in the digital world. 
                I pay close attention to detail and am always eager to learn. 
                I work on both front-end and back-end development to 
                ensure smooth user experiences and strong functionality. 
                I have a solid foundation in coding languages and frameworks 
                and am committed to improving my skills and staying updated on new technologies. 
                My dedication to learning and problem-solving drives me towards becoming
                a skilled and adaptable developer in the constantly changing tech industry.
                </p>
                <h2 className="italic font-semibold  text-center mt-10">For more check <Link to="/about" className='text-red-600 hover:text-red-800'>FAQS</Link></h2>
            </div>
        </motion.div>
    );
}

export default About;

