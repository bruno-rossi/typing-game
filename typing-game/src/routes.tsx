import App from "./App";
import ErrorPage from "./pages/ErrorPage";
import Home from "./pages/Home";

const routes = [
    {
        path: '/',
        element: <App />,
        errorElement: <ErrorPage />,
        children: [
            {
                path: '/',
                element: <Home />
            }
        ]
    }
]

export default routes;
