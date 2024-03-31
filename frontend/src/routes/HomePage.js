import React, { Suspense } from "react";
import './HomePage.css'

const FrontPage = React.lazy(() => import("../components/HomePageComponents/FrontPage"));
const NavBar = React.lazy(() => import("../components/CommonComponents/NavBar"));
const About = React.lazy(() => import("../components/HomePageComponents/About"));
const Skills = React.lazy(() => import("../components/HomePageComponents/Skill"));

const App = () => {
  return (
    <div className="h-screen w-screen bg-white overflow-y-auto overflow-x-hidden bg-gradient-to-tr from-green-900 to-green-100 overflow-hidden">
      <Suspense fallback={<div>Loading...</div>}>
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
        <div className="h-full min-h-full min-w-full w-full overflow-hidden overflow-y-hidden">
          <Skills />
        </div>
        </Suspense>
    </div>
  )
}

export default App;
