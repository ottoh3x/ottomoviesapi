from fastapi import FastAPI
import uvicorn

from MoviesApi import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def main():
    return "Hello Friend!"


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

@app.get('/api/latest_movies')
def latest_movies():
    latest_movies = HomeMoviesApi.latestMovies(None)
    return latest_movies

@app.get('/api/episode/{movie_id}')
def movie_episode(movie_id : str):
    movie_episode = HomeMoviesApi.moviesEpisode(movie_id=movie_id)
    return movie_episode


if __name__== "__main__":
   uvicorn.run(app, host="127.0.0.1", port=8080)

