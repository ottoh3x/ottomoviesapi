from bs4 import BeautifulSoup
import requests


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0",
}


class HomeMoviesApi():
    def __init__(self, movie_id):
        self.movie_id = movie_id

    def trendingMovies(self):
        links = []
        url = "https://lookmoviess.com"
        r = requests.get(url).text
        soup = BeautifulSoup(r, 'html.parser')
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
        links = {}
        url = f"https://lookmoviess.com/movie/{movie_id}"
        r = requests.get(url).text
        soup = BeautifulSoup(r, "html.parser")
        iframe = soup.find(id="iframe-embed")['src']
        links['iframe'] = iframe
        return links
