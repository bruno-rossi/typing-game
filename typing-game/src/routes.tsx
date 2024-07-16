import App from "./App";
import ErrorPage from "./pages/ErrorPage";
import MainMenu from "./pages/MainMenu";

const routes = [
    {
        path: '/',
        element: <App />,
        errorElement: <ErrorPage />,
        children: [
            {
                path: '/',
                element: <MainMenu />
            },
            {
                path: '/new-game/',
                element: <MainMenu />
            },
            {
                path: '/stats/',
                element: <MainMenu />
            },
            {
                path: '/levels/',
                element: <MainMenu />
            },
            {
                path: '/players/',
                element: <MainMenu />
            }
        ]
    }
]

export default routes;
