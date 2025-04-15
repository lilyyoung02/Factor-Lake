from MarketObject import load_data, MarketObject
from portfolio import Portfolio
from CalculateHoldings import rebalance_portfolio
from FactorFunction import Momentum6m, ROE, ROA
import pandas as pd
import logging
import argparse
### ADDING LOGGER INFO TO ALLOW FOR DYNAMIC UPDATES
parser = argparse.ArgumentParser()
parser.add_argument('--verbosity', type=str, default='INFO')
args = parser.parse_args()

# Set up logging
logger = logging.getLogger()
logger.handlers = []
handler = logging.StreamHandler()
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(getattr(logging, args.verbosity.upper()))


def main():
    ### Load market data ###
    print("Loading market data...")
    rdata = load_data()

    ### Data preprocessing ###
    print("Processing market data...")
    rdata['Ticker'] = rdata['Ticker-Region'].dropna().apply(lambda x: x.split('-')[0].strip())
    rdata['Year'] = pd.to_datetime(rdata['Date']).dt.year
    rdata = rdata[['Ticker', 'Ending Price', 'Year',  'ROE using 9/30 Data', 'ROA using 9/30 Data', '6-Mo Momentum %']]
    factors = [Momentum6m(), ROE(), ROA()]

    ### Rebalancing portfolio across years ###
    print("Rebalancing portfolio...")
    final_portfolio = rebalance_portfolio(rdata, factors, start_year=2002, end_year=2023, initial_aum=1)

if __name__ == "__main__":
    main()
