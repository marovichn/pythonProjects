import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline>a')
scores = soup.select('.score')
hrefs = []
texts = []

for link in links:
    hrefs.append(f'{link.get_text()} : {link.get('href')}')

for score in scores:
    texts.append(score.get_text())

res = {}
for key in hrefs:
    for text in texts:
        res[key] = text
        texts.remove(text)
        break

filtered_res = {k: v for k, v in res.items() if int(v.split()[0]) >= 50}
sorted_res = dict(sorted(filtered_res.items(), key=lambda item: int(item[1].split()[0]), reverse=True))

print(sorted_res)
