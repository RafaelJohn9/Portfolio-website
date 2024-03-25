import React from 'react';
import './GlowBalls.css'; // Assuming you have a CSS file for styling

const GlowBalls = () => {
    return (
        <div className="inset-0 flex flex-col items-center justify-center  overflow-hidden flex-grow">
            <div className=" flex overflow-hidden flex-grow flex-wrap gap-32">
                <div className="glow-ball-green"></div>
                <div className="glow-ball-green"></div>
                <div className="glow-ball-green"></div>
                <div className="glow-ball-green"></div>
                <div className="glow-ball-green"></div>
                <div className="glow-ball-green"></div>
                <div className="glow-ball-green"></div>
                <div className="glow-ball-green"></div>
                
            </div>
        </div>
    );
};

export default GlowBalls;