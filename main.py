from MarketObject import load_data, MarketObject
from portfolio import Portfolio
from CalculateHoldings import rebalance_portfolio
from UserInput import get_factors
import pandas as pd

# Set up logging to clean up output
import argparse
import logging
from LoggerConfiguration import get_logger, setup_root_logger

parser = argparse.ArgumentParser()
parser.add_argument('--verbosity', type=str, default='INFO', help='Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)')
args = parser.parse_args()
level = getattr(logging, args.verbosity.upper())

setup_root_logger(level)
logger = get_logger(__name__)
logger.debug("✅ DEBUG from main.py confirmed")



def main():
    ### Load market data ###
    print("Loading market data...")
    rdata = load_data()

    ### Data preprocessing ###
    print("Processing market data...")
    rdata['Ticker'] = rdata['Ticker-Region'].dropna().apply(lambda x: x.split('-')[0].strip())
    rdata['Year'] = pd.to_datetime(rdata['Date']).dt.year
    available_factors = ['ROE using 9/30 Data', 'ROA using 9/30 Data', '12-Mo Momentum %', '6-Mo Momentum %', '1-Mo Momentum %', 'Price to Book Using 9/30 Data', 'Next FY Earns/P', '1-Yr Price Vol %', 'Accruals/Assets', 'ROA %', '1-Yr Asset Growth %', '1-Yr CapEX Growth %', 'Book/Price', 'Next-Year\'s Return %', 'Next-Year\'s Active Return %']
    rdata = rdata[['Ticker', 'Ending Price', 'Year'] + available_factors]
    factors = get_factors(available_factors)

    ### Rebalancing portfolio across years ###
    logger.info("Rebalancing portfolio...")
    final_portfolio = rebalance_portfolio(rdata, factors, start_year=2002, end_year=2023, initial_aum=1)

if __name__ == "__main__":
    main()
