from bs4 import BeautifulSoup
import aiohttp
import asyncio

import requests


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0",
}


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            r = await res.text()
            return r

class HomeMoviesApi():
    def __init__(self, movie_id):
        self.movie_id = movie_id

    def trendingMovies(self):
        links = []
        results = asyncio.run(fetch("https://lookmoviess.com/"))
        soup = BeautifulSoup(results, 'html.parser')
        trending_movies = soup.find(id="trending-movies")
        for i in trending_movies.find_all('div', 'flw-item'):
            image = i.img['data-src']
            url = i.a['href']
            title = i.h3.text
            year = i.find('span', 'fdi-item').text
            duration = i.find('span', 'fdi-item fdi-duration').text
            type = i.find('span', 'float-right fdi-type').text
            links.append({'title': title.strip(),
                          'image': image,
                          'year': year,
                          'type': type,
                          'duration': duration,
                          'url': f"https://lookmoviess.com{url}"

                          })
        return links

    def trendingTV(self):
        links = []
        url = "https://lookmoviess.com"
        r = requests.get(url).text
        soup = BeautifulSoup(r, 'html.parser')
        trending_tv = soup.find(id="trending-tv")
        for i in trending_tv.find_all('div', 'flw-item'):
            image = i.img['data-src']
            url = i.a['href']
            title = i.h3.text
            fdi_items = i.find_all('span', 'fdi-item')
            season = fdi_items[0].text
            eps = fdi_items[1].text
            mv = i.find('span', 'float-right fdi-type').text
            links.append({'title': title.strip(),
                          'image': image,
                          'season': season,
                          'eps': eps,
                          'type': mv,
                          'url': f"https://lookmoviess.com{url}"

                          })
        return links

    def popularMovies(self):
        links = []
        url = "https://lookmoviess.com"
        r = requests.get(url).text
        soup = BeautifulSoup(r, 'html.parser')
        popular_movies = soup.find(id="popular-movies")
        for i in popular_movies.find_all('div', 'flw-item'):
            image = i.img['data-src']
            url = i.a['href']
            title = i.h3.text
            year = i.find('span', 'fdi-item').text
            duration = i.find('span', 'fdi-item fdi-duration').text
            type = i.find('span', 'float-right fdi-type').text
            links.append({'title': title.strip(),
                          'image': image,
                          'year': year,
                          'type': type,
                          'duration': duration,
                          'url': f"https://lookmoviess.com{url}"

                          })
        return links

    def popularTV(self):
        links = []
        url = "https://lookmoviess.com"
        r = requests.get(url).text
        soup = BeautifulSoup(r, 'html.parser')
        popular_tv = soup.find(id="popular-tv")
        for i in popular_tv.find_all('div', 'flw-item'):
            image = i.img['data-src']
            url = i.a['href']
            title = i.h3.text
            fdi_items = i.find_all('span', 'fdi-item')
            season = fdi_items[0].text
            eps = fdi_items[1].text
            mv = i.find('span', 'float-right fdi-type').text
            links.append({'title': title.strip(),
                          'image': image,
                          'season': season,
                          'eps': eps,
                          'type': mv,
                          'url': f"https://lookmoviess.com{url}"

                          })
        return links

    def latestMovies(self):
        links = []
        url = "https://lookmoviess.com"
        r = requests.get(url).text
        soup = BeautifulSoup(r, 'html.parser')
        l = soup.find_all("div", "film_list-wrap")
        latest_movies = l[4]
        for i in latest_movies.find_all('div', 'flw-item'):
            image = i.img['data-src']
            url = i.a['href']
            title = i.h3.text
            year = i.find('span', 'fdi-item').text
            duration = i.find('span', 'fdi-item fdi-duration').text
            type = i.find('span', 'float-right fdi-type').text
            links.append({'title': title.strip(),
                          'image': image,
                          'year': year,
                          'type': type,
                          'duration': duration,
                          'url': f"https://lookmoviess.com{url}"

                          })
        return links

    def latestTV(self):
        links = []
        url = "https://lookmoviess.com"
        r = requests.get(url).text
        soup = BeautifulSoup(r, 'html.parser')
        l = soup.find_all("div", "film_list-wrap")
        latest_tv = l[5]
        for i in latest_tv.find_all('div', 'flw-item'):
            image = i.img['data-src']
            url = i.a['href']
            title = i.h3.text
            fdi_items = i.find_all('span', 'fdi-item')
            season = fdi_items[0].text
            eps = fdi_items[1].text
            mv = i.find('span', 'float-right fdi-type').text
            links.append({'title': title.strip(),
                          'image': image,
                          'season': season,
                          'eps': eps,
                          'type': mv,
                          'url': f"https://lookmoviess.com{url}"


                          })

        return links

    def moviesEpisode(movie_id):
        data = []
        links = {}
        url = f"https://lookmoviess.com/movie/{movie_id}"
        r = requests.get(url).text
        soup = BeautifulSoup(r, "html.parser")
        iframe = soup.find(id="iframe-embed")['src']
        details = soup.find('div',"detail_page-infor")
        title = details.find("h2","heading-name").text
        imdb = details.find('button','btn-imdb').text.replace(' ',"").replace("IMDB:",'')
        trailer = soup.find(id="iframe-trailer")['data-src']
        image = details.find('img')['src']
        description = details.find('div','description').text.strip()
        released = details.find_all('div','row-line')[0].text.replace(" ","").replace("Released:","")
        released = released.strip()
        duration = details.find_all('div','row-line')[3].text.replace(" ","").replace("Duration:","")
        duration = duration.strip()
        links['title'] = title
        links['imdb'] = imdb
        links['trailer'] = trailer
        links['image'] = image
        links['description'] = description
        links['released'] = released
        links['duration'] = duration
        links['iframe'] = iframe
        data.append(links)
        genre = details.find_all('div','row-line')[1]
        for x in genre.find_all('a'):
            url = x['href']
            genre = x['title']
            data.append({"genres" :{"url": url, "genre": genre}})

        casts = details.find_all('div','row-line')[2]
        for x in casts.find_all('a'):
            url = x['href']
            title = x['title']
            data.append({"casts" :{"url": url, "title": title}})
        
        country = details.find_all('div','row-line')[4]
        for x in country.find_all('a'):
            url = x['href']
            country = x['title']
            data.append({"countries" :{"url": url, "country": country}})
        production = details.find_all('div','row-line')[5]
        for x in production.find_all('a'):
            url = x['href']
            title = x['title']
            data.append({"productions" :{"url": url, "title": title}})

        

        

        return data

movie = HomeMoviesApi.moviesEpisode(movie_id="the-innocents-85632")
print(movie)