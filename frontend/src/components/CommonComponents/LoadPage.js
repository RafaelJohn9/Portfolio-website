import React from 'react';
import { motion } from "framer-motion";

const LoadPage = () => {
    return (
        <div className="loading min-h-screen min-w-screen h-screen w-screen flex items-center justify-center md:gap-24 gap-12  md:mx-8">
            <motion.div className=" bg-gradient-to-tr from-[#16552f] to-[#d0f2dc] w-8 h-8 md:w-32 md:h-32 rounded-full" animate={{ scale: [1, 2, 1] }} transition={{ duration: 1, ease: "easeInOut", repeat: Infinity }}></motion.div>
            <motion.div className=" bg-gradient-to-tr from-[#16552f] to-[#d0f2dc] w-8 h-8 md:w-32 md:h-32 rounded-full" animate={{ scale: [1, 2, 1] }} transition={{ duration: 1, ease: "easeInOut", repeat: Infinity, delay: 0.2 }}></motion.div>
            <motion.div className=" bg-gradient-to-tr from-[#16552f] to-[#d0f2dc] w-8 h-8 md:w-32 md:h-32 rounded-full" animate={{ scale: [1, 2, 1] }} transition={{ duration: 1, ease: "easeInOut", repeat: Infinity, delay: 0.4 }}></motion.div>
        </div>
    );
};

export default LoadPage;