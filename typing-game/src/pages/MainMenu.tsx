import { useNavigate } from "react-router-dom";

function MainMenu(): JSX.Element {

    const navigate = useNavigate();

    function handleButtonClick(event: React.MouseEvent<HTMLButtonElement>) {
        // Write new game logic here
        navigate(`/${event.currentTarget.id}/`);
    }

    function handleSecondaryButtonClick(event: React.MouseEvent<HTMLButtonElement>) {
        navigate(`/${event.currentTarget.id}/`);
    }

    return (
        <div className="main">
            <div id="main-menu">
                <h1>Main Menu</h1>
                <button className="button primary" id="new-game" onClick={e => handleButtonClick(e)}>New Game</button>
                <button className="button secondary" id="stats" onClick={e => handleSecondaryButtonClick(e)}>Stats</button>
                <button className="button secondary" id="levels" onClick={e => handleSecondaryButtonClick(e)}>List of levels</button>
                <button className="button secondary" id="players" onClick={e => handleSecondaryButtonClick(e)}>List of players</button>
            </div>
        </div>
    )
}

export default MainMenu;