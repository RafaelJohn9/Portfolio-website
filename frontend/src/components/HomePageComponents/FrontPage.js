import React from "react";
import './FrontPage.css';
import { motion } from "framer-motion";

const FrontPage = () => {
  return (
    <div className="h-full w-full text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-custom flex items-center justify-center relative overflow-hidden">
      <motion.div className="absolute w-40 h-40 bg-green-900 rounded-full animate-pulse opacity-20 blur-lg" 
        animate={{ scale: [0.9, 1.1], opacity: [0.1, 0.6] }} 
        transition={{ duration: 2, repeat: Infinity, repeatType: "reverse" }} 
      />
      <motion.div className="absolute w-32 h-32 bg-green-900 rounded-full animate-pulse opacity-20 blur-lg" 
        style={{ top: "30%", left: "10%" }} 
        animate={{ scale: [0.8, 1.2], opacity: [0.1, 0.6] }} 
        transition={{ duration: 3, repeat: Infinity, repeatType: "reverse" }} 
      />
      <motion.div className="absolute w-24 h-24 bg-green-900 rounded-full animate-pulse opacity-20 blur-lg" 
        style={{ bottom: "20%", right: "10%" }} 
        animate={{ scale: [0.7, 1.3], opacity: [0.1, 0.6] }} 
        transition={{ duration: 4, repeat: Infinity, repeatType: "reverse" }} 
      />
      <motion.div className="absolute w-20 h-20 bg-green-900 rounded-full animate-pulse opacity-20 blur-lg" 
        style={{ top: "20%", right: "20%" }} 
        animate={{ scale: [0.6, 1.4], opacity: [0.1, 0.6] }} 
        transition={{ duration: 5, repeat: Infinity, repeatType: "reverse" }} 
      />
      <motion.div className="absolute w-20 h-20 bg-green-900 rounded-full animate-pulse opacity-20 blur-lg" 
        style={{ top: "70%", right: "50%" }} 
        animate={{ scale: [0.9, 1.4], opacity: [0.1, 0.6] }} 
        transition={{ duration: 5, repeat: Infinity, repeatType: "reverse" }} 
      />
      <motion.div className="absolute w-20 h-20 bg-green-900 rounded-full animate-pulse opacity-20 blur-lg" 
        style={{ top: "70%", left: "10%" }} 
        animate={{ scale: [3.6, 2.4], opacity: [0.1, 0.6] }} 
        transition={{ duration: 5, repeat: Infinity, repeatType: "reverse" }} 
      />
        <motion.div className="absolute w-20 h-20 bg-green-900 rounded-full animate-pulse opacity-20 blur-lg" 
        style={{ top: "10%", right: "10%" }} 
        animate={{ scale: [3.6, 2.4], opacity: [0.1, 0.6] }} 
        transition={{ duration: 5, repeat: Infinity, repeatType: "reverse" }} 
      />
      <div className="flex items-center justify-center self-center flex-col z-10">
        <div className="w-full h-full flex items-center justify-center text-center flex-col">
          <img src="https://media4.giphy.com/media/26xBwdIuRJiAIqHwA/giphy.webp?cid=ecf05e47wdhkf6a4ueqdda15rr9hc26j2uuxokkx2ad2ici8&ep=v1_gifs_search&rid=giphy.webp&ct=g"
          alt="Animated GIF" className="w-64 h-64 rounded-full" />
          <h1> Hi, I am John, a Junior FullStack Engineer</h1>
        </div>
      </div>
    </div>
  )
};



export default FrontPage;