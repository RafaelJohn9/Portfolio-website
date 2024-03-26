import React from 'react';
import './InfiniteHorizontalScroll.css'

const InfiniteHorizontalScroll = ({ children }) => {
  return (
    <div className="overflow-x-auto whitespace-nowrap">
      <div className="inline-flex animate-scroll">
        {children}
        {children} {/* Repeat children for seamless looping */}
      </div>
    </div>
  );
};

export default InfiniteHorizontalScroll;
