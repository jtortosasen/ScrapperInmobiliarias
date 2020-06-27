# class enalquiler_selectors:
#     articles = '#body > div.container.grid > div.main.relative > ul > li.property-item'
#     street = 'div.property-info-wrapper > div:nth-child(2) > div.property-info-location.ellipsis-element-control'
#     url = 'div.property-info-wrapper > div:nth-child(1) > div.property-info-title.ellipsis-element-control > a'
#     price = 'div.property-info-wrapper > div:nth-child(1) > div.property-info-price > span'
#     description = 'div.property-info-wrapper > div:nth-child(2) > div.property-info-description.hidden-xs'
#     date_posted = 'div.property-img-wrapper > div > ul > li'
#     agency = 'div.property-img-wrapper > div > div.property-agency-brand > div > img'
#     phone = ''


import re
import datetime, pytz

def enalquiler_callback(soup):
    minute = ['minuto', 'minute']
    hour = ['hora', 'hour']
    day = ['dia', 'day', 'día']

    items = []
    items_container = soup.find("ul", {"class": "property-list list-unstyled"})
    for article in items_container.find_all("li", {"itemtype": "http://schema.org/Product"}):
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
            street = article.find("div", {"class": "property-info-location ellipsis-element-control"}).text.strip()
        except Exception:
            pass
        try:
            url = article.find("a", {"itemprop": "url"})['href'].strip()
        except Exception:
            pass
        try:
            text = article.find("span", {"class": "info-price"}).text.strip()
            if isinstance(text, int):
                price = text
            else:
                price = int(re.findall(r"\d+", text.replace('.', ''))[0])
        except Exception:
            pass
        try:
            description = article.find("div", {"class": "property-info-description hidden-xs"}).text.strip()
        except Exception:
            pass
        try:
            string = article.find("li", {"class": "property-tag-new"})['uib-tooltip'].strip()
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
            agency = article.find("div", {"class": "linkstyle"})['title'].strip()
        except Exception:
            pass

        try:
            articleImageUrl = article.find("div", {"class": "property-img-wrapper"}).find("picture").find("img", {"class": "property-img-background"})['srcset']
        except Exception:
            pass

        try:
            temp = article.find("div", {"class":"property-agency-brand"}).find("div", {"class": "linkstyle"})
            agencyImageUrl = temp.find("img")['src']
        except Exception as e:
            pass

        items.append({
            'street': street,
            'url': url,
            'price': price,
            'description': description,
            'datePosted': date_posted,
            'phone': phone,
            'agency': agency,
            'websiteName': 'enalquiler',
            'articleImageUrl': articleImageUrl,
            'agencyImageUrl': agencyImageUrl
        })
    return items