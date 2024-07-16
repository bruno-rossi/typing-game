import React from 'react';
import NavBar from './components/NavBar';
import Footer from './components/Footer';
import { Outlet } from 'react-router-dom';
import { useState } from 'react';
import { Player } from './types/types';

function App() {

  const [ player, setPlayer ] = useState<Player | null>(null);

  return (
    <div className="App">
        <NavBar />
        <Outlet context={{player: player, setPlayer: setPlayer}} />
        <Footer />
    </div>
  );
}

export default App;
