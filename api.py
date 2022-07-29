from fastapi import FastAPI
from MoviesApi import *

app = FastAPI()


@app.get('/api/trending_movies')
def trending_movies():
    trending_movies = HomeMoviesApi.trendingMovies(None)
    return trending_movies


@app.get('/api/trending_tv')
def trending_tv():
    trending_tv = HomeMoviesApi.trendingTV(None)
    return trending_tv


@app.get('/api/popular_movies')
def popular_movies():
    popular_movies = HomeMoviesApi.popularMovies(None)
    return popular_movies


@app.get('/api/popular_tv')
def popular_tv():
    popular_tv = HomeMoviesApi.popularTV(None)
    return popular_tv

@app.get('/api/popular_movies')
def popular_movies():
    popular_movies = HomeMoviesApi.popularMovies(None)
    return popular_movies  