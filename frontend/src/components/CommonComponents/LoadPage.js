import React from 'react';

const LoadPage = () => {

    return (
      <div className="w-full h-full flex justify-center items-center">
        <div className='w-2/5 h-2/5 flex justify-center items-center rounded-full'>
          <iframe src="https://giphy.com/embed/iQaJmNecCFyJNnpMxi" title='loading' width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
        </div>
      </div>
    );
};

export default LoadPage;