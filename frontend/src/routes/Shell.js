import React, { useEffect, useRef } from 'react';
import Terminal from 'terminal.js';

function Shell() {
  const terminalRef = useRef(null);

  useEffect(() => {
    const terminal = new Terminal({
      cursorBlink: true, // Enable cursor blinking
      convertEol: true, // Convert '\n' to '\r\n' on output
      rows: 20, // Number of rows
      cols: 80, // Number of columns
      screenKeys: true, // Enable special keys such as F1, F2, arrow keys, etc.
      useStyle: true, // Apply default styling
      scrollback: 1000, // Number of scrollback lines
      tabStopWidth: 8, // Width of tab characters
      fontFamily: 'Courier', // Font family
      fontSize: 14, // Font size in pixels
      bellStyle: 'sound', // Bell sound
      bellSound: 'lib/term/sounds/ding', // Path to the bell sound
    });

    // Mount the terminal to the DOM
    terminal.open(terminalRef.current);

    // Handle terminal resize
    const handleResize = () => {
      terminal.fit();
    };

    // Attach resize event listener
    window.addEventListener('resize', handleResize);

    // Initialize terminal dimensions
    handleResize();

    // Clean up function
    return () => {
      terminal.destroy();
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  return <div ref={terminalRef}></div>;
}

export default Shell;
