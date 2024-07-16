import React from 'react';
import NavBar from './components/NavBar';
import Footer from './components/Footer';
import Home from './pages/Home';
import { Outlet } from 'react-router-dom';

function App() {
  return (
    <div className="App">
        <NavBar />
        <Outlet />
        <Footer />
    </div>
  );
}

export default App;
