import React from "react";
import FrontPage from "./components/FrontPage";
import NavBar from "./components/NavBar";

const App = () => {
  return (
    <div className="h-screen w-screen bg-gradient-to-br from-blue-900 to-black overflow-auto">
      <NavBar />
      <FrontPage />
    </div>
  )
}


export default App;