###commenting this out to avoid conflicts in colab notebook - molly
##from google.colab import drive
##drive.mount('/content/drive')

import pandas as pd
import numpy as np

### CREATING FUNCTION TO LOAD DATA ###
def load_data():
    file_path = '/content/drive/My Drive/Cayuga Fund Factor Lake/FR2000 Annual Quant Data FOR RETURN SIMULATION.xlsx'
    rdata = pd.read_excel(file_path, sheet_name='Data', header=2, skiprows=[3, 4])

    return rdata

class MarketObject():
    def __init__(self, data, t):
        """
        data(Dataframe):    column 1 being 'Ticker', column 2 being 'Ending Price'
        t(Datetime):        Date of market data, 
        """
        self.stocks = data.dropna()
        self.stocks.rename(columns = {self.stocks.columns[0]: 'Ticker', self.stocks.columns[1]: 'Ending Price'}, inplace = True)
        self.t = t

    def getPrice(self, ticker):
        ticker_data = self.stocks.loc[self.stocks['Ticker'] == ticker]

        #check to see if results are empty - molly
        if ticker_data.empty:
            print(f"{ticker} - not found in market data for {self.t} - SKIPPING")
            return None

        #if the data exists, return the last row's ending price - molly 
        return ticker_data['Ending Price'].iloc[-1]

### MOVED THIS TO PORTFOLIO.PY ###
#data = rdata.copy()
#data['Ticker'] = data['Ticker-Region'].dropna().apply(lambda x: x[0:x.find('-')])
#data['Year'] = pd.to_datetime(data['Date']).dt.year
#data = data[['Ticker', 'Ending Price', 'Year']]

#marketObject_2002 = MarketObject(data.loc[data['Year'] == 2002], 2002)
#marketObject_2003 = MarketObject(data.loc[data['Year'] == 2003], 2003)
#print('price of AOS in 2002 = ' + str(marketObject_2002.getPrice('AOS')))
#print('price of AOS in 2003 = ' + str(marketObject_2003.getPrice('AOS')))
