# class idealista_selectors:
    # articles    = '#main-content > div.items-container > article'
    # street      = 'div > div > div.item-info-container > a'
    # url         = 'div > div > div.item-info-container > a'
    # price       = 'div > div > div.item-info-container > div.row.price-row.clearfix > span.item-price.h2-simulated'
    # description = 'div > div > div.item-info-container > span:nth-last-child(n+4)'
    # date_posted = 'div > div > div.item-info-container > span:nth-child(6)'
    # agency      = 'div > div > div.item-info-container > div.logo-branding > a'
    # phone       = 'div > div > div.item-info-container > div.item-toolbar.clearfix > div.item-toolbar-contact > span'

import re
import datetime, pytz

def idealista_callback(soup):
    minute = ['minuto', 'minute']
    hour = ['hora', 'hour']

    items = []
    items_container = soup.find("div", {"class": "items-container"})
    for article in items_container.find_all("article", {"class": None}):
        street = ''
        url = ''
        price = 0
        description = ''
        date_posted = ''
        phone = ''
        agency = ''
        articleImageUrl = ''
        agencyImageUrl = ''


        try:
            street = article.find("a", {"class": "item-link"}).text
        except Exception:
            pass
        try:
            url = ''.join(['https://idealista.com', article.find("a", {"class": "item-link"})['href']])
        except Exception:
            pass
        try:
            text = int(re.sub('[^0-9]', '', article.find('span', {'class': 'item-price h2-simulated'}).text.strip()))
            if isinstance(text, int):
                price = text
            else:
                price = int(re.findall(r"\d+", text.replace('.', ''))[0])
        except Exception as e:
            pass
        try:
            description =  ' '.join([a.text for a in article.find_all('span', {'class': 'item-detail'})[:-1]])
        except Exception:
            pass
        try:
            posted_time = ''
            string = ''.join([a.text for a in article.find_all('span', {'class': 'item-detail'})[-1:]]).strip()
            if minute[0] in string or minute[1] in string:
                current_time = datetime.datetime.now()
                posted_time = (current_time - datetime.timedelta(minutes=int(re.sub('[^0-9]', '', string)))).replace(
                    microsecond=0)
            if hour[0] in string or hour[1] in string:
                current_time = datetime.datetime.now()
                posted_time = (current_time - datetime.timedelta(hours=int(re.sub('[^0-9]', '', string)))).replace(
                    microsecond=0)
            date_posted = str(posted_time.astimezone(pytz.utc))
        except Exception:
            pass
        try:
            phone = article.find("span", {"class": "icon-phone item-not-clickable-phone"}).text
        except Exception:
            pass


        try:
            agency = ''
            if article.find("a", {"data-xiti-click": "listado::logo-agencia"}) is not None:
                agency = article.find("a", {"data-xiti-click": "listado::logo-agencia"})['title']
                # temp = article.find("a", {"data-xiti-click": "listado::logo-agencia"})
                # agencyImageUrl = temp.find("img", attrs={"data-ondemand-img": True})['src']
        except Exception:
            pass

        # try:
        #     articleImageUrl = article.find("img", {"class": "vertical"})['src']
        # except Exception:
        #     pass

        items.append({
            'street': street,
            'url': url,
            'price': price,
            'description': description,
            'datePosted': date_posted,
            'phone': phone,
            'agency': agency,
            'websiteName':'idealista',
            'articleImageUrl': articleImageUrl,
            'agencyImageUrl': agencyImageUrl
        })

    return items

# def _start_crawl(self, url):

