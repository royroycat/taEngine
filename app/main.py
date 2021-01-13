import schedule
import time
import requests
import numpy as np
from classes.ta_engine import TAEngine
import ast

def runVolumeComparePercentageIndex():
    # get all stock ticker from API
    r = requests.get('http://whomentionstock_uwsgi-nginx-flask_1:80/stock')
    stock_array = ast.literal_eval(r.text)
    msg = '(LastDayVolume - 21AverageVolume) / 21AverageVolume) * 100\n==========\n'
    # create TAEngine for each ticker
    for ticker in stock_array:
        tickerEngine = TAEngine(ticker)
        index = tickerEngine.volumeComparePercentageIndex()
        msg += '%s : %f%%\n' % (ticker, index)
    print(msg)
    sendTelegram(msg)
    pass

def sendTelegram(msg):
    url = 'http://whomentionstock_uwsgi-nginx-flask_1:80/telegram'
    arg = {'msg': msg}
    requests.post(url, data = arg)
    pass

schedule.every().day.at("01:01").do(runVolumeComparePercentageIndex)

while True:
    schedule.run_pending()
    time.sleep(1)