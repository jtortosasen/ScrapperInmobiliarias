from crawler.crawler import Crawler

url = 'https://www.habitaclia.com/alquiler-viviendas-ascensor_amueblado_-barcelona.htm?ordenar=mas_recientes&&hab=1&coddists=400st=1,4,9,11,13,'
result = Crawler(url).crawl()
# file = open('result.py', 'w')
# file.write(str(result))
# file.close()
print(result)
