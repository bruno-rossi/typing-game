function NavBar(): JSX.Element {
    return (
        <div id="nav">
            <h1 className="logo">Typing Game</h1>
            <ul className="settings-ul">
                <li className="settings-li">Light mode</li>
                <li className="settings-li">Keyboard layout</li>
                <li className="settings-li">Language</li>
            </ul>
        </div>
    )
}

export default NavBar;