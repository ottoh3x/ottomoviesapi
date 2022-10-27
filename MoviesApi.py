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
    def __init__(self, movie_id, page,animeid):
        self.movie_id = movie_id
        self.page = page
        self.animeid = animeid
    
    def anime(animeid):
        data = []
        r = requests.get(f"https://animetitans.com/anime/{animeid}")
        soup = BeautifulSoup(r.text, "html.parser")
        body = soup.find('div', 'postbody')
        title = body.find('h1', 'entry-title').text
        synopsis = body.find('div', 'synp').find('div','entry-content').p.text
        image_url = body.find('div', 'thumb').img['src']
        image_cover = body.find('div', 'bigcover').img['src']
        info = body.find('div', 'spe')
        content_info = info.find_all('span')
        status = content_info[0].text.replace("الحالة: ",'')
        studio = content_info[1].text.replace("الاستديو: ",'')
        year = content_info[2].text.replace("سنة الإصدار: ",'')
        duration = content_info[3].text.replace("المدة: ",'')
        season = content_info[4].text.replace("الموسم: ",'')
        country = content_info[5].text.replace("البلد: ",'')
        typee = content_info[6].text
        episodes = content_info[7].text.replace("الحلقات: ",'')
        directors = content_info[8].text.replace("المخرج: ",'')
        date_release = content_info[9].text.replace("تاريخ النشر: ",'')
        genres = []
        g = body.find('div', 'genxed')
        for x in g.find_all('a'):
            genres.append(x.text) 
        r = body.find('div','listupd')
        recommendation = []
        for x in r.find_all('article'):
            anime_id = x.a['href']
            t = x.a['title']
            img = x.a.img['src']
            typee = x.find('div','typez').text
            recommendation.append({
                "id":anime_id,
                "title":t,
                "image_url":img,
                "type":typee
            
            })
            

        data.append({
            "title":title,
            "synopsis":synopsis,
            "image_url":image_url,
            "image_cover":image_cover,
            "status":status,
            "studio":studio,
            "year":year,
            "duration":duration,
            "season":season,
            "country":country,
            "type":typee,
            "episodes":episodes,
            "directors":directors,
            "date_release":date_release,
            "genres":genres,
            "recommendation":recommendation
        })
        return data

    def Movies(page):
        data = []
        url = f"https://lookmoviess.com/movies?page={page}"
        r = requests.get(url).text
        soup = BeautifulSoup(r, 'html.parser')
        mv = soup.find_all('div', 'flw-item')
        for x in mv:
            id = x.find('a')['data-id']
            url = x.find('a')['href']
            title = x.find('h3', 'film-name').text.strip()
            image = x.find('img')['data-src']
            duration = x.find('span', "fdi-duration").text
            type = x.find('span', 'fdi-type').text
            year = x.find('span', 'fdi-item').text
            data.append({"title": title,
                         "id": id,
                         'url': f"https://lookmoviess.com{url}",
                         "image": image,
                         "duration": duration,
                         "type": type,
                         "year": year,

                         })
        return data

    def TV(page):
        data = []
        url = f"https://lookmoviess.com/tv-shows?page={page}"
        r = requests.get(url).text
        soup = BeautifulSoup(r, 'html.parser')
        mv = soup.find_all('div', 'flw-item')
        for i in mv:
            image = i.img['data-src']
            url = i.a['href']
            id = i.a['data-id']
            title = i.h3.text
            fdi_items = i.find_all('span', 'fdi-item')
            season = fdi_items[0].text
            eps = fdi_items[1].text
            mv = i.find('span', 'float-right fdi-type').text
            data.append({'title': title.strip(),
                         'image': image,
                         'season': season,
                         'eps': eps,
                         'type': mv,
                         'id': id,
                         'url': f"https://lookmoviess.com{url}", })

        return data

    def TOPIMDBMOVIES(page):
        data = []
        url = f"https://lookmoviess.com/top-imdb?type=movie&page={page}"
        r = requests.get(url).text
        soup = BeautifulSoup(r, 'html.parser')
        mv = soup.find_all('div', 'flw-item')
        for x in mv:
            id = x.find('a')['data-id']
            url = x.find('a')['href']
            title = x.find('h3', 'film-name').text.strip()
            image = x.find('img')['data-src']
            duration = x.find('span', "fdi-duration").text
            type = x.find('span', 'fdi-type').text
            year = x.find('span', 'fdi-item').text
            data.append({"title": title,
                         "id": id,
                         'url': f"https://lookmoviess.com{url}",
                         "image": image,
                         "duration": duration,
                         "type": type,
                         "year": year,

                         })
        return data

    def TOPIMDBTV(page):
        data = []
        url = f"https://lookmoviess.com/top-imdb?type=tv&page={page}"
        r = requests.get(url).text
        soup = BeautifulSoup(r, 'html.parser')
        mv = soup.find_all('div', 'flw-item')
        for i in mv:
            image = i.img['data-src']
            url = i.a['href']
            id = i.a['data-id']
            title = i.h3.text
            fdi_items = i.find_all('span', 'fdi-item')
            season = fdi_items[0].text
            eps = fdi_items[1].text
            mv = i.find('span', 'float-right fdi-type').text
            data.append({'title': title.strip(),
                         'image': image,
                         'season': season,
                         'eps': eps,
                         'type': mv,
                         'id': id,
                         'url': f"https://lookmoviess.com{url}", })

        return data


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
        c = []
        g = []
        p = []
        co = []
        url = f"https://lookmoviess.com/movie/{movie_id}"
        r = requests.get(url).text
        soup = BeautifulSoup(r, "html.parser")
        iframe = soup.find(id="iframe-embed")['src']
        details = soup.find('div', "detail_page-infor")
        title = details.find("h2", "heading-name").text
        imdb = details.find(
            'button', 'btn-imdb').text.replace(' ', "").replace("IMDB:", '')
        trailer = soup.find(id="iframe-trailer")['data-src']
        image = details.find('img')['src']
        description = details.find('div', 'description').text.strip()
        released = details.find_all(
            'div', 'row-line')[0].text.replace(" ", "").replace("Released:", "")
        released = released.strip()
        duration = details.find_all(
            'div', 'row-line')[3].text.replace(" ", "").replace("Duration:", "")
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
        genre = details.find_all('div', 'row-line')[1]
        for x in genre.find_all('a'):
            url = x['href']
            genre = x['title']
            g.append({"genres": {"url": url, "genre": genre}})

        casts = details.find_all('div', 'row-line')[2]
        for x in casts.find_all('a'):
            url = x['href']
            title = x['title']
            c.append({"casts": {"url": url, "title": title}})

        country = details.find_all('div', 'row-line')[4]
        for x in country.find_all('a'):
            url = x['href']
            country = x['title']
            co.append({"countries": {"url": url, "country": country}})
        production = details.find_all('div', 'row-line')[5]
        for x in production.find_all('a'):
            url = x['href']
            title = x['title']
            p.append({"productions": {"url": url, "title": title}})

        return data, c, g, p, co

    def tvEpisode(tv_id):
        links = {}
        data = []
        season = []
        c = []
        g = []
        p = []
        co = []
        url = f"https://lookmoviess.com/tv/{tv_id}"
        r = requests.get(url).text
        soup = BeautifulSoup(r, "html.parser")
        iframe = soup.find(id="iframe-embed")['src']
        tmdb_id = soup.find(id="watch-iframe")['data-tmdb-id']
        s = soup.find('div', 'sl-content')
        seasons = s.find('ul', 'slcs-ul').find_all('li')
        for x in seasons:
            t = []
            title = x.find('a', 'season-item')['title']
            year = x.find('span', 'float-right').text
            id = x.find('a', 'season-item')['href'].replace("#", "")
            episodes = s.find('div', 'slc-eps')
            eps = episodes.find(id=id).find_all('li')
            season.append({

                "title": title,
                "year": year,
                "episodes": t

            })
            for x in eps:
                episode_num = x.find('a', 'episode-item')['data-number']
                href = x.find('a', 'episode-item')['href']
                season_num = x.find('a', 'episode-item')['data-s-number']
                episode_title = x.find('a', 'episode-item')['title']
                t.append({"episode_title": episode_title,
                          "episode_num": episode_num,
                          "href": href,
                          "season_num": season_num})

        details = soup.find('div', "detail_page-infor")
        title = details.find("h2", "heading-name").text
        imdb = details.find(
            'button', 'btn-imdb').text.replace(' ', "").replace("IMDB:", '')
        trailer = soup.find(id="iframe-trailer")['data-src']
        image = details.find('img')['src']
        description = details.find('div', 'description').text.strip()
        released = details.find_all(
            'div', 'row-line')[0].text.replace(" ", "").replace("Released:", "")
        released = released.strip()
        duration = details.find_all(
            'div', 'row-line')[3].text.replace(" ", "").replace("Duration:", "")
        duration = duration.strip()
        links['title'] = title
        links['imdb'] = imdb
        links['trailer'] = trailer
        links['image'] = image
        links['description'] = description
        links['released'] = released
        links['duration'] = duration
        links['iframe'] = iframe
        links['tmdb_id'] = tmdb_id
        data.append(links)
        genre = details.find_all('div', 'row-line')[1]
        for x in genre.find_all('a'):
            url = x['href']
            genre = x['title']
            g.append({"genres": {"url": url, "genre": genre}})

        casts = details.find_all('div', 'row-line')[2]
        for x in casts.find_all('a'):
            url = x['href']
            title = x['title']
            c.append({"casts": {"url": url, "title": title}})

        country = details.find_all('div', 'row-line')[4]
        for x in country.find_all('a'):
            url = x['href']
            country = x['title']
            co.append({"countries": {"url": url, "country": country}})
        production = details.find_all('div', 'row-line')[5]
        for x in production.find_all('a'):
            url = x['href']
            title = x['title']
            p.append({"productions": {"url": url, "title": title}})

        return data, season, c, p, co, g
