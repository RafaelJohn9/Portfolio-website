import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import  './index.css';

const renderApp = () => {
  return ReactDOM.render(<App />, document.getElementById('root'));
};

renderApp();
