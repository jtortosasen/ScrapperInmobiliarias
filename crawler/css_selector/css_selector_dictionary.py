from crawler.css_selector.idealista_selectors import idealista_callback
from crawler.css_selector.enalquiler_selectors import enalquiler_callback
from crawler.css_selector.fotocasa_selectors import fotocasa_callback
from crawler.css_selector.habitaclia_selectors import habitaclia_callback

def websites_callbacks(website):
    return {
        'fotocasa': fotocasa_callback,
        'idealista': idealista_callback,
        'habitaclia': habitaclia_callback,
        'enalquiler': enalquiler_callback,
    }[website]

list_websites = [
    'fotocasa',
    'idealista',
    'habitaclia',
    'enalquiler',
]


