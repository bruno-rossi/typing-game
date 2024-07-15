import App from './components/App.tsx';
import Home from './pages/Home.tsx';
import ErrorPage from './pages/ErrorPage.tsx';

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