import requests
from bs4 import BeautifulSoup
import re
import json


regex = r':\s*\n+'
subst = ": "


gen_ani_res = [{}]

p = {}
blabla = []
links = []
eps = {}
url = "https://lookmoviess.com/tv/peaky-blinders-39230"
r = requests.get(url).text
soup = BeautifulSoup(r, 'html.parser')
s1 = soup.find('div', 'seasons-list')
t = s1.text
for x in s1.find_all('a', 'season-item'):
    sea = x['title']
    idep = x['href'].replace('#', "").strip().replace(
        " ", '').replace("\n", "")
    blabla.append(idep)
    
    for b in s1.find(id=idep):
        f = b.find('a')
        print(f)
        # titre = b['title']
        # ur = b['href']
        # epi = b['data-number']
        # season = b["data-s-number"]
        # print(sea)
        # print(titre)
        # print(ur)
        # print(epi)
        # print(season)
            

        # for t in ep.find_all('a'):
        #     print(t)
        
        # titre = x['title']
        # ur = x['href']
        # epi = x['data-number']
        # season = x["data-s-number"]
#             # print(titre)
#             # print(ur)
#             # print(epi)
#             # print(season)
#         links.append({
    
#             "ep":epi,
#             "title":titre,
#             "url":ur
#             })

# print(links)

    # links.append({
    #     "season" : season,
    #     "eps" : {}
    # })




#     links.append({'title':titre,
# 'url':ur,
# "episode":epi,
# "numberOfEpisodes":numEpisodes})
# for x in s1.find_all(id=idep):
#     h = x.find_all('a')

# # for x in ep.find_all('li','nav-item'):
# #     print(x.text)
# print(links)

y = {
    'season': "Season 1",
    'eps': {
        "title": "Episode 1 : First"
    }
}
