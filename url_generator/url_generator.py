import importlib
import threading

from url_generator.site_dictionary.sites_dictionary import list_keywords

criterion_words = [
    "id",
    "province",
    "property",
    "city",
    "district",
    "maximumPrice",
    "minimumPrice",
    "bedroom",
    "bathroom",
    "extraFilter",
    "dwelling",
    "equipment",
    "pet"
]


class CriterionException(Exception):
    pass


def _isdictionary(ob):
    return isinstance(ob, dict)


class Generator(object):
    def __init__(self, criterion):
        self.criterion = criterion
        self.lock = threading.Lock()
        self.urls = {}

    def _check_criterion(self, criterion):
        for key, value in criterion.items():
            if key not in criterion_words:
                return False

    def generate_urls(self):
        if (self.criterion == None):
            raise CriterionException('Criterion is None')
        elif self._check_criterion(self.criterion):
            raise CriterionException('Invalid criterion')
        else:
            self._start_threads()
        return self.urls

    def _start_threads(self):
        threads = set(
            threading.Thread(target=self._generate_url, args=(list_keywords, i)) for i, k in enumerate(list_keywords))
        # threads = []
        # threads.append(threading.Thread(target=self._generate_url, args=(list_websites, 0)))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

    def _extract_site_dictionary(self, keywords, i):
        module = importlib.import_module("url_generator.site_dictionary.{}".format(keywords[i]))
        return getattr(module, keywords[i])

    def _generate_url(self, list_websites, list_index):
        array_values = []
        website_dictionary = self._extract_site_dictionary(list_websites, list_index)
        ignored_keys = []
        for key, value in website_dictionary.items():
            if not self._key_ignored(key, ignored_keys):
                if self._is_criterion(key):
                    extracted_value = self._get_criterion_value(key, value, ignored_keys)
                    array_values.extend(extracted_value)
                else:
                    array_values.extend(value)
        url = self._assembly_url(array_values)
        url = self._fix_url(url)
        with self.lock:
            self.urls[list_websites[list_index]] = url

    def _key_ignored(self, key, ignored):
        return key in ignored

    def _is_criterion(self, key):
        return key in criterion_words

    def _get_criterion_value(self, key, value, ignored_keys):
        if _isdictionary(value):
            return self._extract_dictionary_value(key, value, ignored_keys)
        else:
            return self._get_formatted_value(key, value)

    def _assembly_url(self, array):
        return ''.join(array)

    def _fix_url(self, url):
        if url[-1] == ';':
            url = url[:-1]

        return url

    def _extract_dictionary_value(self, key, value, ignored_dict_keys):
        nested_criterion_words = self._extract_nested_criterion_words(value)
        if not self._isempty(nested_criterion_words):
            nested_value = self._nested_criterion_value(nested_criterion_words, value)
            if nested_value is None:
                return self._get_value(key, value)
            else:
                ignored_dict_keys.append(nested_value['key'])
                return nested_value['value']
        else:
            return self._get_value(key, value)

    def _extract_nested_criterion_words(self, value):
        words = []
        for key in value.keys():
            if _isdictionary(key):
                if self._is_criterion(key):
                    words.append(key)
        return words

    def _nested_criterion_value(self, words, value):
        temp = None
        for word in words:
            if _isdictionary(value[word]):
                temp = {'value': self._get_value(word, value[word]), 'key': word}
            else:
                temp = {'value': self._get_formatted_value(word, value[word]), 'key': word}
        return temp

    def _get_value(self, key, value):
        val = ''
        if bool(self.criterion[key]):
            if isinstance(self.criterion[key], list):
                val = []
                for c in self.criterion[key]:
                    try:
                        val.append(value[c])
                    except KeyError:
                        pass
            else:
                try:
                    val = value[self.criterion[key]]
                except KeyError:
                    pass
        return val if bool(val) else ''

    def _get_formatted_value(self, key, value):
        val = ''
        try:
            if bool(self.criterion[key]):
                val = value.format(self.criterion[key])
        except KeyError:
            pass
        return val

    def _isempty(self, array):
        return bool(array)


if __name__ == '__main__':
    pass
