import threading
import timeit

from crawler.crawler import Crawler
from url_generator.url_generator import Generator

dict = {
    "id": 1,
    "province": "barcelona",
    "property": "dwelling",
    "city": "barcelona",
    "district": 'surroundings_of_barcelona',
    "maximumPrice": '1300',
    "minimumPrice": '',
    "bedroom": '',
    "bathroom": '',
    "extraFilter": ["elevator"],
    # "extraFilter": "elevator",
    "dwelling": "studio",
    "equipment": "furnished",
    "pet": False
}

result = []
lock = threading.Lock()


def go(url):
    r = Crawler(url).crawl()
    with lock:
        result.extend(r)


if __name__ == '__main__':
    start = timeit.default_timer()
    urls = Generator(dict).generate_urls()
    t_array = []

    for url in urls:
        t = threading.Thread(target=go, args=(url,))
        t_array.append(t)

    for i in range(len(urls)):
        t_array[i].start()

    for i in range(len(urls)):
        t_array[i].join()

    stop = timeit.default_timer()
    print('Time: ', stop - start)

    with open('result.py', 'w') as f:
        for item in result:
            f.write("%s\n" % item)
