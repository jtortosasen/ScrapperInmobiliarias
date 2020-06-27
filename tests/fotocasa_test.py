import requests
from bs4 import BeautifulSoup

from crawler.css_selector.fotocasa_selectors import fotocasa_callback

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "es,en-US;q=0.9,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Refer": "https://www.google.es/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
url = 'https://www.fotocasa.es/es/alquiler/casas/barcelona-capital/barri-gotic/l?sortType=publicationDate&latitude=41.38266930099403&longitude=2.176401576049409&combinedLocationIds=724,9,8,232,376,8019,0,1152,350&gridType=3'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'lxml')
print(fotocasa_callback(soup))
