from MarketObject import MarketObject, load_data
import pandas as pd
import logging 
import ipywidgets as widgets

### setting up loggin package to clean up the output and to allow user to pick level of detail of output
logger = logging.getLogger()
logger.handlers = []
handler = logging.StreamHandler()
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

### adding custom labels to the verbosity options
custom_to_logging = {'Main Data': 'CRITICAL', 'Summary Only': 'INFO','Detailed': 'DEBUG',}

verbosity_dropdown = widgets.Dropdown(
    options=list(custom_to_logging.keys()),
    value='Summary Only',
    description='Verbosity:',
)

class Factors:
    def get(ticker, market):
        return "Factor not specified"

class Momentum6m(Factors):
    def get(self, ticker, market):
        ticker_data = market.stocks.loc[market.stocks['Ticker'] == ticker]

        #check to see if results are empty - molly
        if ticker_data.empty:
            logger.debug(f"{ticker} - not found in market data for {market.t} - SKIPPING")
            #print(f"{ticker} - not found in market data for {market.t} - SKIPPING")
            return None
        #column in excel sheet is called: 6-Mo Momentum %
        try:
            value = ticker_data['6-Mo Momentum %'].iloc[-1]
            return value
        except (KeyError, IndexError) as e:
            logger.debug(f"Error accessing 6-Mo Momentum % for {ticker}: {e}")
            #print(f"Error accessing 6-Mo Momentum % for {ticker}: {e}")
            return None

class ROE(Factors):
    def get(self, ticker, market):
        ticker_data = market.stocks.loc[market.stocks['Ticker'] == ticker]

        #check to see if results are empty - molly
        if ticker_data.empty:
            logger.debug(f"{ticker} - not found in market data for {market.t} - SKIPPING")
            #print(f"{ticker} - not found in market data for {market.t} - SKIPPING")
            return None
        #column in excel sheet is called: 6-Mo Momentum %
        try:
            value = ticker_data['ROE using 9/30 Data'].iloc[-1]
            return value
        except (KeyError, IndexError) as e:
            logger.debug(f"Error accessing 6-Mo Momentum % for {ticker}: {e}")
            return None

class ROA(Factors):
    def get(self, ticker, market):
        ticker_data = market.stocks.loc[market.stocks['Ticker'] == ticker]

        #check to see if results are empty - molly
        if ticker_data.empty:
            logger.debug(f"{ticker} - not found in market data for {market.t} - SKIPPING")
            #print(f"{ticker} - not found in market data for {market.t} - SKIPPING")
            return None
        #column in excel sheet is called: 6-Mo Momentum %
        try:
            value = ticker_data['ROA using 9/30 Data'].iloc[-1]
            return value
        except (KeyError, IndexError) as e:
            logger.debug(f"Error accessing 6-Mo Momentum % for {ticker}: {e}")
            return None

#Creating an Example
if __name__ == "__main__":
    rdata = load_data()
    rdata.columns = rdata.columns.str.strip()
    rdata = rdata.loc[:, ~rdata.columns.duplicated(keep='first')]
    rdata['Ticker'] = rdata['Ticker-Region'].dropna().apply(lambda x: x.split('-')[0].strip())
    rdata['Date'] = pd.to_datetime(rdata['Date'])
    rdata['Year'] = rdata['Date'].dt.year

    df_2002 = rdata[rdata['Year'] == 2002].copy()
    df_2003 = rdata[rdata['Year'] == 2003].copy()

    marketObject_2002 = MarketObject(df_2002, 2002)
    marketObject_2003 = MarketObject(df_2003, 2003)


    # EXAMPLE USING Factors CLASS 
    Momentum6m_2002_FLWS = Factors.Momentum6m("FLWS", marketObject_2002)
    Momentum6m_2002_AAPL = Factors.Momentum6m("AAPL", marketObject_2002)

    print(f'\n6 Month Momentum Value of FLWS in 2002: ' + str(Momentum6m_2002_FLWS))
    print(f'6 Month Momentum Value of AAPL in 2002: ' + str(Momentum6m_2002_AAPL))

