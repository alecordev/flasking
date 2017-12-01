import time
import logging
import threading
from functools import wraps

import pandas as pd
import requests
from flask import Flask


fmt = '[%(asctime)s] - [%(process)d:%(processName)s | %(thread)d:%(threadName)s] - %(message)s'
logging.basicConfig(level=logging.DEBUG,
                    format=fmt)
app = Flask(__name__)


def timing(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        t0 = time.time()
        result = f(*args, **kwargs)
        t1 = time.time()
        logging.debug('{} with [{}, {}] - Took: {:2.4f} seconds'.format(f.__name__, args, kwargs, t1 - t0))
        return result
    return wrap


@timing
def read_data():
    while 1:
        logging.info('Reading data file...')
        # df = pd.read_excel('some_data.xlsx')
        df = pd.read_csv('some_data.csv')
        logging.info('Done reading.')
        logging.info(len(df))
        time.sleep(10)


@timing
def main():
    read_data()


def heartbeat():
    logging.info('Sleeping a bit')
    time.sleep(5)
    while 1:
        logging.info(requests.get('http://localhost:5050').status_code)
        time.sleep(1)


@app.route('/')
def index():
    return 'ok'


if __name__ == '__main__':
    # threading.Thread(target=main, daemon=True).start()
    threading.Thread(target=heartbeat, daemon=True).start()
    app.run(host='0.0.0.0', port=5050, debug=False, threaded=True)
