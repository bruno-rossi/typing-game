import { useNavigate } from "react-router-dom";
import { useState } from "react";
import NewPlayerModal from "../components/NewPlayerModal";

function MainMenu(): JSX.Element {

    const navigate = useNavigate();
    // const modal = document.getElementById("modal") as HTMLDivElement;
    // modal.style.display = "none";

    function handleNewGameClick(event: React.MouseEvent<HTMLButtonElement>) {
        // Write new game logic here
        // modal.style.display = "inline-block";
        // navigate(`/${event.currentTarget.id}/`);
        return
    }

    function handleSecondaryButtonClick(event: React.MouseEvent<HTMLButtonElement>) {
        navigate(`/${event.currentTarget.id}/`);
    }

    function startNewGame() {
        console.log("Game started");
    }

    return (
        <div className="main">
            <div id="main-menu">
                <NewPlayerModal />
                <h1>Main Menu</h1>
                <button className="button primary" id="new-game" onClick={e => handleNewGameClick(e)}>New Game</button>
                <button className="button secondary" id="stats" onClick={e => handleSecondaryButtonClick(e)}>Stats</button>
                <button className="button secondary" id="levels" onClick={e => handleSecondaryButtonClick(e)}>List of levels</button>
                <button className="button secondary" id="players" onClick={e => handleSecondaryButtonClick(e)}>List of players</button>
            </div>
        </div>
    )
}

export default MainMenu;