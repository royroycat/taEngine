import yfinance as yf
from ta.volume import OnBalanceVolumeIndicator

class TAEngine:
    
    def __init__(self, ticker):
        self.ticker = ticker
        self.yfObject = yf.Ticker(self.ticker)
        
    # 1. Take average of this 21days volume
    # 2. Cal today OBV using with the previous 21days data
    # 3. todayObv / average21Vol
    # If index is + and huge mean big volume buying and up
    # If index is - and huge mean big volume selling and down 
    def volumeComparePercentageIndex(self):
        hist = self.yfObject.history(period="22d")
        average21Vol = hist['Volume'][:-1].mean()
        todayVol = hist['Volume'].tail(1)
        index = ((todayVol - average21Vol) / average21Vol) * 100
        return index