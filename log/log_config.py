import datetime as dt
import logging


class MyFormatter(logging.Formatter):
    converter = dt.datetime.fromtimestamp

    def formatTime(self, record, datefmt=None):
        ct = self.converter(record.created)
        if datefmt:
            s = ct.strftime(datefmt)
        else:
            t = ct.strftime("%H:%M:%S")
            s = "%s,%03d" % (t, record.msecs)
        return s


formatter = MyFormatter(
    fmt='[%(levelname)s] %(asctime)s: %(filename)s:%(lineno)d --:%(message)s',
)

logger = logging.getLogger(__name__)
# file_handler = log.FileHandler('debug.log')
# logger.addHandler(file_handler)
# file_handler.setFormatter(formatter)
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)