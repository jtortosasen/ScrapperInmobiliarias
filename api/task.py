from log.log_config import logger
import threading

from crawler.crawler import Crawler
from url_generator.url_generator import Generator

def search_criterion(criterion):
    _launch_thread(_search_criterion_task, (criterion,))

def search_criteria(criteria):
    _launch_thread(_search_criteria_task, (criteria,))

def api_url(url):
    logger.info(f'changing API URL {static.core_api_url} to {url}')
    static.core_api_url = url

def logging_level(level):
    logger.setLevel(level)

def _launch_thread(job, args):
    thread = threading.Thread(target=job, args=args)
    thread.setDaemon(True)
    thread.start()

def _search_criteria_task(criteria):
    logger.info('creating threads for each criterion')
    for criterion in criteria:
        _launch_thread(job=_search_criterion_task, args=(criterion,))

def _search_criterion_task(criterion):
    logger.info('getting urls')
    urls = _generate_urls(criterion=criterion)
    results = {'searchCriterionId': criterion['id'], 'contents': []}
    logger.info('starting search_criterion_job pool threads per url')
    for website, url in urls.items():
        _launch_thread(job=_search_criterion_job, args=(url, results))
    logger.info(f'sending results from {str(criterion)} to API')
    sender.search_results(results)

def _generate_urls(criterion):
    return Generator(criterion).generate_urls()

def _search_criterion_job(url, list_result):
    result = Crawler(url).crawl()
    logger.debug(f'per {url} getting {str(len(result))} results')
    with threading.Lock():
        list_result['contents'].extend(result)

from api import sender
from api import static