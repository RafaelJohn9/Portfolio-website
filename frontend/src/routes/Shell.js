import React, { useState } from 'react';
import postCommand from '../middleware/shell' 
import NavBar from '../components/CommonComponents/NavBar';


const Output = ({ result }) => {
    return (
        <div className='flex flex-wrap w-screen h-28'>
          {result}
        </div>
    )
};

const Shell = () => {
  const [inputValue, setInputValue] = useState('');
  const [outputResult, setOutputResult] = useState('');

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleEnterKeyPress = async (event) => {
    if (event.key === 'Enter') {
      const result = await processCommand(inputValue.trim());
      setOutputResult(result);
      setInputValue(''); // Clear the input field after processing the command
    }
  };

  const processCommand = async (command) => {
    // Simulate processing the command
    let result;
    switch (command) {
      case 'help':
        result = 'List of available commands: - help - greet Common linux commands like: ls, echo, whoami, etc';
        break;
      case 'greet':
        result = 'Hello! Welcome to the web terminal!';
        break;
      default:
        result = await postCommand(command);
        console.log(result);
        result = Object.values(result).join('\n');
    }
    return result;
  };

  return (
    <div className="flex flex-col h-screen min-h-screen bg-gray-900 text-white flex-wrap">
      <NavBar />
      <div className="flex mt-24">
        <span className="text-green-500 mr-2">$</span>
        <input
          className="flex-1 bg-gray-900 text-white rounded outline-none"
          type="text"
          value={inputValue}
          onChange={handleInputChange}
          onKeyDown={handleEnterKeyPress}
        />
      </div>
      <Output result={outputResult} />
    </div>
  );
};

export default Shell;
