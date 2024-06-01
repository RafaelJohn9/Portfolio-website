import React from 'react';
import hourGlass from '../../imgs/hourglass.gif'

const LoadPage = () => {

    return (
      <div className="w-full h-full flex justify-center items-center">
        <div className='w-2/5 h-2/5 flex justify-center items-center rounded-full'>
          <img src={hourGlass} alt='' width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></img>
        </div>
      </div>
    );
};

export default LoadPage;
