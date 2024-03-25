import React from 'react';
import star from '../imgs/icons8-star.gif'; // replace with the actual path to your star image

const Star = () => {
    return (
        <div className="flex">
            <img src={star} alt="star" className="w-12 h-12" />
            <img src={star} alt="star" className="w-12 h-12" />
            <img src={star} alt="star" className="w-12 h-12" />
            <img src={star} alt="star" className="w-12 h-12" />
            <img src={star} alt="star" className="w-12 h-12" />
        </div>
    );
};

export default Star;