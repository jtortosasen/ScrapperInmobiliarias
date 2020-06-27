import requests
from bs4 import BeautifulSoup

from crawler.css_selector.css_selector_dictionary import websites_callbacks, list_websites


class Crawler(object):

    def __init__(self, url):
        self.url = url

    def crawl(self):
        response = self._get_html()
        soup = BeautifulSoup(response.content, 'lxml')
        callback = self._site_html_crawler()
        self.website = self._get_website()
        crawl_result = self._start_crawl(soup, callback)
        return crawl_result

    def _get_html(self):
        headers = self._generate_header()
        return requests.get(self.url, headers=headers)

    def _site_html_crawler(self):
        callback = self._websites_callback()
        if callback is None:
            raise Exception('Incorrect or unsuported URL')
        return callback

    def _get_website(self):
        for website in list_websites:
            if website in self.url:
                return website

    def _start_crawl(self, soup, callback):
        result = ''
        try:
            result = callback(soup)
            return result
        except Exception as e:
            print(e, self.website)
            return result

    def _websites_callback(self):
        for website in list_websites:
            if website in self.url:
                return websites_callbacks(website)

    def _generate_header(self):
        return {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "utf-8, gzip, deflate, br",
            "Accept-Language": "es,en-US;utf-8;q=0.9,en;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Refer": "https://www.google.es/",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
        }
