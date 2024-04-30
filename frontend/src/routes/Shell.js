import React, { useEffect, useRef, useState, useCallback } from 'react';
import { Terminal } from 'xterm';
import 'xterm/css/xterm.css';
import postCommand from '../middleware/shell';

const Shell = () => {
  const [userData, setUserData] = useState("");
  const [terminal, setTerminal] = useState(null); // Define terminal state

  const terminalRef = useRef(null);

  const handleData = useCallback(async (data) => {
    if (/^[a-zA-Z0-9\s\-/\\"'&|[\]{}()$<>.,]+$/.test(data)) {
      terminal.write(data);
      await setUserData(prevData => prevData + data);
      console.log(userData);
    }
  }, [terminal, userData]);

  const handleBackspace = useCallback(async (e) => {
    if (e.domEvent.key === 'Backspace') {
      const activeLine = userData;
      if (activeLine.length > 2) {
        terminal.write('\b \b');
        await setUserData(prevData => prevData.slice(0, -1));
        console.log(userData);
      }
    }
  }, [terminal, userData]);

  useEffect(() => {
    var data = ""
    const term = new Terminal();
    term.open(terminalRef.current);
    term.focus();
    term.prompt = () => {
      term.write("$ ");
    };
    term.prompt();

    term.onData(async (data) => {
      await handleData(data);
    });

    term.onKey(async (e) => {
      await handleBackspace(e);
      if (e.domEvent.key === 'Enter') {
        term.write('\n\r');
        setUserData((prevData) => {
		data = prevData;
		return ("");
	});
        term.write(await postCommand(data));
        console.log(userData);
        term.write('\n\r');
        term.prompt();
      } else if (e.domEvent.key === 'ArrowRight') {
        term.write('\x1b[C');
      }
    });

    setTerminal(term); // Set terminal state

    return () => {
      term.dispose();
    };
  }, [handleData, handleBackspace, userData]);

  return (
    <div className='bg-black h-screen w-screen flex flex-grow flex-col overflow-hidden'>
      <div className='h-full w-full bg-black overflow-x-hidden' ref={terminalRef}></div>
    </div>
  );
};

export default Shell;
