import requests
from bs4 import BeautifulSoup

from crawler.css_selector.habitaclia_selectors import habitaclia_callback

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
url = 'https://www.habitaclia.com/alquiler-madrid.htm?ordenar=mas_recientes'
minute = ['minuto', 'minute']
hour = ['hora', 'hour']
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'lxml')
print(habitaclia_callback(soup))
