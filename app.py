import logging
from aiohttp import web
from log.log_config import logger
from api.routes import setup_routes
import threading

lock = threading.Lock()

logger.setLevel(logging.INFO)
app = web.Application()
setup_routes(app)

web.run_app(app)

if __name__ == '__main__':
    pass