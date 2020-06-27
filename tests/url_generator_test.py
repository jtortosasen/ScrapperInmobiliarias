import threading
import timeit

from url_generator.url_generator import Generator

dict = {
    "id": 1,
    "province": "barcelona",
    "property": "dwelling",
    "city": "barcelona",
    "district": "les_corts",
    "maximumPrice": '',
    "minimumPrice": '',
    "bedroom": "one",
    "bathroom": "one",
    "extraFilter": ["elevator"],
    # "extraFilter": "elevator",
    "dwelling": "flat",
    "equipment": "furnished",
    "pet": False
}
criterion_words = [
    "id",
    "province",
    "property",
    "city",
    "district",
    "maxPrice",
    "minPrice",
    "bedroom",
    "bathroom",
    "extraFilter",
    "dwelling",
    "equipment",
    "pet"
]

result = []
lock = threading.Lock()


def with_threads():
    r = Generator(dict).generate_urls()
    with lock:
        result.extend(r)


if __name__ == '__main__':
    start = timeit.default_timer()
    t_array = []
    t_size = 1
    for i in range(t_size):
        t = threading.Thread(target=with_threads)
        t_array.append(t)

    for i in range(t_size):
        t_array[i].start()

    for i in range(t_size):
        t_array[i].join()

    stop = timeit.default_timer()
    print('Time: ', stop - start)
    print(len(result))
    print(result)
