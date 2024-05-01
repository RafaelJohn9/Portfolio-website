import React, { useEffect, useRef, useState } from 'react';
import { Terminal } from 'xterm';
import 'xterm/css/xterm.css';
import postCommand from '../middleware/shell';

const Shell = () => {
  const terminalRef = useRef(null);
  const terminal = useRef(null); // Store terminal instance using useRef
  const [userInput, setUserInput] =  useState("");
  let userCommand = ""
  const cache = useRef({}); // Create a cache using useRef

  useEffect(() => {
    // Create a new terminal instance
    terminal.current = new Terminal();
    terminal.current.open(terminalRef.current);
    terminal.current.focus();

    // Custom prompt

    terminal.current.prompt = async () => {
      let pwd = (await getCachedResponse("pwd")).replace(/\n/g, '');
      let user = (await getCachedResponse("whoami")).replace(/\n/g, '');
      let nodename = (await getCachedResponse("uname -n")).replace(/\n/g, '');
      terminal.current.write(`${user}@${nodename}:${pwd}$ `);
    };

    const getCachedResponse = async (command) => {
      if (cache.current[command]) {
      return cache.current[command]; // Return cached response if available
      } else {
      const response = await postCommand(command);
      cache.current[command] = response; // Cache the response
      return response;
      }
    };

    // Event listeners
    const onDataHandler = (data) => {
      const validCharacters = /^[a-zA-Z0-9 ?/\\|"'()<>{}[\]\-_*&^%$~`]+$/;
      if (validCharacters.test(data)) {
      terminal.current.write(data);
      setUserInput(prevInput => (prevInput + data));
      }
    };

    const clearTerminal = () => {
      // Write ANSI escape sequence to clear the terminal
      terminal.current.write('\x1b[2J\x1b[H');
    };
    

    const onKeyHandler = async (e) => {
      if (!terminal.current) return; // Ensure terminal is initialized
    
      
      // if (!core || !buffer || !active) return; // Ensure core, buffer, and active are initialized
      if (e.domEvent.key === 'Enter') {
        terminal.current.write('\n\r');
        if (userCommand === 'clear'){
          clearTerminal();
          userCommand = ""
          return ("");
        }else{
        console.log("command: " + userCommand)
        terminal.current.write(await postCommand(userCommand));
      }
      // eslint-disable-next-line react-hooks/exhaustive-deps
      userCommand = ""
      terminal.current.write('\n\r');
      terminal.current.prompt();
      } else if (e.domEvent.key === 'ArrowRight') {
        terminal.current.write('\x1b[C')
      }else if (e.domEvent.key === 'Backspace') {
        if (userCommand === "") {
          // Do nothing
          return;
        } else {
          userCommand = userCommand.length > 1 ? userCommand.slice(0, -1) : '';
          setUserInput(prevInput => (prevInput.length > 1 ? prevInput.slice(0, -1) : ''))
          console.log("userCommand after delete:", userCommand)
            terminal.current.write('\b \b');
          }
        }
      };
    terminal.current.prompt();
    terminal.current.onData(onDataHandler);
    terminal.current.onKey(onKeyHandler);

    
    return () => {
      terminal.current.dispose();
    };
  }, []);

  const onDataChangeHandler = (data) => {
    const validCharacters = /^[a-zA-Z0-9 ?/\\|"'()<>{}[\]\-_*&^%$~`]+$/;
    if (validCharacters.test(data)) {
    userCommand += data;
    }
  };

  useEffect(() => {
    terminal.current.onData(onDataChangeHandler);
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [userInput]);

  return (
    <div className='bg-black h-screen w-screen flex flex-grow flex-col overflow-hidden'>
      <div className='h-full w-full bg-black overflow-x-hidden' ref={terminalRef}></div>
    </div>
  );
};

export default Shell;
