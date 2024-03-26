import React from 'react';
import {createBrowserRouter, RouterProvider}from 'react-router-dom';
import HomePage from './routes/HomePage';
import Page404 from './routes/404Page';
import LoginPage from './routes/LoginPage'
import RegisterPage from './routes/RegisterPage'
import MoviesSearch from './routes/MoviesSearch';

function App() {
    const router = createBrowserRouter([{
        path: '/',
        element: <HomePage />,
        errorElement: <Page404 />
    },{
        path: '/login',
        element: <LoginPage />,
    },{
        path: '/register',
        element: <RegisterPage />,
    },{
        path: '/movies-search',
        element: <MoviesSearch />,
    },
]);


    return (
        <RouterProvider router={router}>
            {router}
        </RouterProvider>
    );
}

export default App;

