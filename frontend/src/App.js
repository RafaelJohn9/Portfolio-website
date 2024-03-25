import React from "react";
import FrontPage from "./components/FrontPage";
import NavBar from "./components/NavBar";
import About from "./components/About";
import Skill from "./components/Skill";
import './App.css'


const App = () => {
  return (
<div className="h-screen w-screen bg-white overflow-scroll overflow-x-hidden bg-gradient-to-tr from-green-900 to-green-100">
      {/* NavBar */}
      <NavBar />                        
      
      {/* First Section */}
      <div className="h-full w-full min-h-full min-w-full">
        <FrontPage />
      </div>
      
      {/* Second Section */}
      <div className=" h-full min-h-full min-w-full w-full">
        <About />
      </div>

      {/* Third Section */}
      <div className=" h-full min-h-full min-w-full w-full">
        <Skill />
      </div>
    </div>
  )
}


export default App;