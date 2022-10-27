import requests
from bs4 import BeautifulSoup as bs



def anime(animeid):
        data = []
        r = requests.get(f"https://animetitans.com/anime/{animeid}/")
        soup = bs(r.text, "html.parser")
        body = soup.find('div', 'postbody')
        title = body.find('h1', 'entry-title').text
        synopsis = body.find('div', 'synp').find('div','entry-content').p.text
        
        image_cover = body.find('div', 'bigcover').img['src']
        image_url = body.find('div', 'thumb').img['src']
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
        print(image_url)
    

print(anime("noblesse"))