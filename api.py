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

@app.get('/api/anime/{animeid}')
async def movies(animeid:str):
    anime = HomeMoviesApi.anime(animeid=animeid)
    return anime

@app.get('/api/movies/{page}')
async def movies(page:int):
    movies = HomeMoviesApi.Movies(page=page)
    return movies

@app.get('/api/tv-shows/{page}')
async def tvshows(page:int):
    tvshows = HomeMoviesApi.TV(page=page)
    return tvshows
    

@app.get('/api/top-imdb/movies/{page}')
async def topImdbMovies(page:int):
    imdbmovies = HomeMoviesApi.TOPIMDBMOVIES(page=page)
    return imdbmovies

@app.get('/api/top-imdb/tv-shows/{page}')
async def topImdbtv(page:int):
    imdbtv = HomeMoviesApi.TOPIMDBTV(page=page)
    return imdbtv



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

@app.get('/api/movie/{movie_id}')
async def movie_episode(movie_id : str):
    movie_episode = HomeMoviesApi.moviesEpisode(movie_id=movie_id)
    return movie_episode

@app.get('/api/tv/{tv_id}')
async def tv_episode(tv_id : str):
    tv_episode = HomeMoviesApi.tvEpisode(tv_id=tv_id)
    return tv_episode


if __name__== "__main__":
   uvicorn.run(app, host="127.0.0.1", port=8080)

