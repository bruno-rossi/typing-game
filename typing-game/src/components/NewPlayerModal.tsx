import { useState } from "react";
import { useOutletContext } from "react-router-dom";
import { Player } from "../types/types";

function NewPlayerModal(): JSX.Element {

    const { setPlayer }: { setPlayer: (player: Player | null) => void } = useOutletContext();
    const [ playerName, setPlayerName ] = useState<string>("");

    function handleSubmit(event: React.FormEvent<HTMLFormElement>){
        event.preventDefault();

        if (validatePlayerName(playerName)) {
            fetch("http://127.0.0.1:5555/players/", {
                method: "POST",
                headers: {
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    name: playerName,
                })
            })
            .then(response => {
                if (response.ok) {
                    return response.json()
                } else if (response.status === 400) {
                    throw new Error('Failed to create user');
                    // How do we handle this error?
                };
            })
            .then(newPlayer => {
                setPlayer(newPlayer);
                console.log("Player has been set successfully!", newPlayer.name);
            })
            .catch(error => console.log(error))

        } else {
            alert("Name not accepted.");
            setPlayerName("");

        }
    }

    function validatePlayerName(name: string) {

        const regex = /^[a-zA-Z\d\s:\u00C0-\u00FF]*$/;

        if (regex.test(name) && name.length >= 3) {
            return true;

        } else {
            return false;

        }
    }

    return (
        <div id="modal">
            <form onSubmit={handleSubmit}>
                <label htmlFor="player-name">Enter your name: </label>
                <input type="text" id="player-name" placeholder="Enter your name" 
                value={playerName} onChange={e => setPlayerName(e.target.value)}
                required></input>
                <p id="player-name-subtext"></p>
                {/* <input className="button primary" type="submit">Start!</input> */}
            </form>
        </div>
    )
}

export default NewPlayerModal;