# class habitaclia_selectors:
#     articles = '#js-list > section > div > section > article'
#     street = 'div > div > section.list-item-content > p.list-item-location > span'
#     url = 'div > div > section.list-item-content > h3 > a'
#     price = 'div > div > section.list-item-content-second > article > span.font-2'
#     description = 'div > div > section.list-item-content > p.list-item-description'
#     date_posted = 'div > div > section.list-item-content > div.list-item-premium > span'
#     agency = ''
#     phone = ''

import re
import datetime, pytz

def habitaclia_callback(soup):
    minute = ['minuto', 'minute']
    hour = ['hora', 'hour']
    day = ['dia', 'day', 'día']

    items = []
    items_container = soup.find("section", {"class": "list-items-container f-right"})
    for article in items_container.find_all("article", {"class": "js-list-item list-item-container js-item-with-link gtmproductclick "}):
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
            street = article.find("a", {"itemprop": "name"}).text.strip()
        except Exception:
            pass
        try:
            url = article.find("a", {"itemprop": "name"})['href'].strip()
        except Exception:
            pass
        try:
            text = article.find("span", {"itemprop": "price"}).text.strip()
            if isinstance(text, int):
                price = text
            else:
                price = int(re.findall(r"\d+", text.replace('.', ''))[0])
        except Exception:
            pass
        try:
            description = article.find("p", {"itemprop": "description"}).text.strip()
        except Exception:
            pass
        try:
            string = article.find("span", {"class": "list-item-date"}).text.strip()
            posted_time = ''
            if minute[0] in string or minute[1] in string:
                current_time = datetime.datetime.now()
                posted_time = (current_time - datetime.timedelta(minutes=int(re.sub('[^0-9]', '', string)))).replace(
                    microsecond=0)
            if hour[0] in string or hour[1] in string:
                current_time = datetime.datetime.now()
                posted_time = (current_time - datetime.timedelta(hours=int(re.sub('[^0-9]', '', string)))).replace(
                    microsecond=0)
            if day[0] in string or day[1] in string or day[2] in string:
                current_time = datetime.datetime.now()
                posted_time = (current_time - datetime.timedelta(days=int(re.sub('[^0-9]', '', string)))).replace(
                    microsecond=0)
            date_posted = str(posted_time.astimezone(pytz.utc))
        except Exception:
            pass

        try:
            if article.find("img", {"class": "list-item-logo-img js-no-click-item"}) is not None:
                agency = article.find("img", {"class": "list-item-logo-img js-no-click-item"})['title'].strip()
            else:
                agency = ''
        except Exception:
            pass

        try:
            articleImageUrl = article.find('div', {'class': 'slick-slide slick-current slick-active'}).find('img')['src']
        except Exception:
            pass

        try:
            agencyImageUrl = article.find('img', {'class': 'list-item-logo-img js-no-click-item'})['src'][2:]
        except Exception:
            pass

        phone = 'NC/SC'

        items.append({
            'street': street,
            'url': url,
            'price': price,
            'description': description,
            'datePosted': date_posted,
            'phone': phone,
            'agency': agency,
            'websiteName': 'habitaclia',
            'articleImageUrl': articleImageUrl,
            'agencyImageUrl': agencyImageUrl
        })
    return items