import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.sejm.gov.pl/sejm9.nsf/interpelacje.xsp?view=1'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
interpelacje = []

for tr in soup.select('#rContent table tr'):
    tds = tr.select('td')
    print(tds)
    if len(tds) == 4:
        nr = tds[0].text.strip()
        autor = tds[1].text.strip()
        ministerstwo = tds[2].text.strip()
        tytul = tds[3].select_one('a').text.strip()
        link = 'https://www.sejm.gov.pl' + tds[3].select_one('a')['href']
        interpelacja = {'nr': nr, 'autor': autor, 'ministerstwo': ministerstwo, 'tytul': tytul, 'link': link}
        interpelacje.append(interpelacja)

with open('interpelacje.json', 'w') as f:
    json.dump(interpelacje, f)