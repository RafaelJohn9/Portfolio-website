import React from 'react';
import {createBrowserRouter, RouterProvider}from 'react-router-dom';
import HomePage from './routes/HomePage';
import Page404 from './routes/404Page';
import LoginPage from './routes/LoginPage'
import RegisterPage from './routes/RegisterPage'
import MoviesSearch from './routes/MoviesSearch';
import MusicSearch from './routes/MusicSearch';
import Books from './routes/Books';
import AboutPage from './routes/AboutPage';
import MoviesSearched from './routes/MoviesSearched';
import MusicSearched from './routes/MusicSearched';
import BooksSearched from './routes/BooksSearched';
import Shell from './routes/Shell';

function App() {
    const router = createBrowserRouter([
        {
            path: '/',
            element: <HomePage />,
            errorElement: <Page404 />
        },
        {
            path: '/login',
            element: <LoginPage />,
            errorElement: <Page404 />
        },
        {
            path: '/register',
            element: <RegisterPage />,
            errorElement: <Page404 />
        },
        {
            path: '/movies-search',
            element: <MoviesSearch />,
            errorElement: <Page404 />
        },
        {
            path: '/music-search',
            element: <MusicSearch />,
            errorElement: <Page404 />
        },
        {
            path: '/about',
            element: <AboutPage />,
            errorElement: <Page404 />
        },{
            path: '/movies-search/:query',
            element: <MoviesSearched />,
            errorElement: <Page404 />,
        },{
            path: '/music-search/:query',
            element: <MusicSearched />,
            errorElement: <Page404 />,
        },{
            path: '/books-search/:query',
            element: <BooksSearched />,
            errorElement: <Page404 />,
        },{
            path: '/books',
            element: <Books/>,
            errorElement: <Page404 />,
        },{
            path: '/shell',
            element: <Shell />,
            errorElement: <Page404 />,
        },
    ]);


    return (
        <RouterProvider router={router}>
            {router}
        </RouterProvider>
    );
}

export default App;

