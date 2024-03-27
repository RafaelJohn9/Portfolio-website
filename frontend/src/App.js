import React from 'react';
import {createBrowserRouter, RouterProvider}from 'react-router-dom';
import HomePage from './routes/HomePage';
import Page404 from './routes/404Page';
import LoginPage from './routes/LoginPage'
import RegisterPage from './routes/RegisterPage'
import MoviesSearch from './routes/MoviesSearch';
import MusicSearch from './routes/MusicSearch';
import BookSearch from './routes/BookSearch';
import AboutPage from './routes/AboutPage';

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
    },{
        path: '/music-search',
        element: <MusicSearch />,
    },{
        path: '/books-search',
        element: <BookSearch />,
    },{
        path: '/about',
        element: <AboutPage />,
    },
]);


    return (
        <RouterProvider router={router}>
            {router}
        </RouterProvider>
    );
}

export default App;

