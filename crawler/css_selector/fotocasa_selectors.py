# class fotocasa_selectors:
#     articles    = '#App > div > div.re-Searchpage > div.re-Searchpage-wrapper > div.re-Searchresult-wrapper > div.re-Searchresult > div'
#     street      = 'div > div > div.sui-CardComposable-secondary > div > a > div.re-Card-wrapperTitle > div.re-Card-meta > h3'
#     url         = 'div > div > div.sui-CardComposable-secondary > div > a'
#     price       = 'div > div > div.sui-CardComposable-secondary > div > a > div.re-Card-priceContainer > div > span.re-Card-price > span'
#     description = 'div > div > div.sui-CardComposable-secondary > div > a > span'
#     date_posted = 'div > div > div.sui-CardComposable-secondary > div > a > div.re-Card-wrapperTitle > div.re-Card-bumpdate > span.re-Card-timeago'
#     agency      = 'div > div > div.sui-CardComposable-secondary > div > div.re-Card-promotionLogo > a > img'
#     phone       = 'div > div > div.sui-CardComposable-secondary > div > div.re-Card-contact > a > span > span.sui-AtomButton-text'

import datetime, pytz
import re


def fotocasa_callback(soup):
    minute = ['minuto', 'minute']
    hour = ['hora', 'hour']
    day = ['dia', 'day', 'día']

    items = []
    items_container = soup.find("div", {"class": "re-Searchresult"})
    try:
        articles = items_container.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['re-Searchresult-itemRow'])
        for i, article in enumerate(articles):

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
                street = article.find("h3", {"class": "re-Card-title"}).text
            except Exception:
                pass
            try:
                url = ''.join(['https://fotocasa.es', article.find("a", {"class": "re-Card-link"})['href'].strip()])
            except Exception:
                pass
            try:
                pricespan = article.find("span", {"class": "re-Card-price"})
                text = pricespan.find("span").text.strip()
                if isinstance(text, int):
                    price = text
                else:
                    price = int(re.findall(r"\d+", text.replace('.', ''))[0])
            except Exception:
                pass
            try:
                description = article.find("span", {"class": "re-Card-description"}).text.strip()
            except Exception:
                pass
            try:
                string = article.find("span", {"class": "re-Card-timeago"}).text.strip()
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
                if article.find("a", {"class": "re-CardImage-link"}) is not None:
                    # agency = article.find("div", {"class": "linkstyle"})['title'].strip()
                    agency = 'Yes'
                else:
                    agency = ''
            except Exception:
                pass
            try:
                if article.find('span', {'class': 'sui-AtomButton-text'}) is not None:
                    phone = article.find('span', {'class': 'sui-AtomButton-text'}).text
                else:
                    phone = ''
            except Exception:
                pass

            try:
                articleImageUrl = article.find('li', {'class': 'react-Slidy-item'}).find('img', {'class': 're-CardImage-image'})['src']
            except Exception:
                pass

            try:
                agencyImageUrl = article.find('div', {'class': 're-Card-promotionLogo'}).find('img', {'class': 're-CardImage-image'})['src']
            except Exception:
                pass

            items.append({
                'street': street,
                'url': url,
                'price': price,
                'description': description,
                'datePosted': date_posted,
                'phone': phone,
                'agency': agency,
                'websiteName': 'fotocasa',
                'articleImageUrl': articleImageUrl,
                'agencyImageUrl': agencyImageUrl
            })
    except:
        pass
    return items
