import time
print("✅ main() reached!", flush=True)
time.sleep(1)

from MarketObject import load_data, MarketObject
from portfolio import Portfolio
from CalculateHoldings import rebalance_portfolio
from UserInput import get_factors
import pandas as pd
import argparse
# Use custom verbosity manager
from verbosity_state import vb

# parser = argparse.ArgumentParser()
# parser.add_argument('--verbosity', type=str, default='INFO')
# args = parser.parse_args()
# vb.set_level(args.verbosity)  # Set selected verbosity level
parser = argparse.ArgumentParser()
parser.add_argument('--verbosity', type=str, default='INFO')
parser.add_argument('--fasttest', action='store_true', help='Run a short simulation')  # ✅ this line is key
args = parser.parse_args()

vb.set_level(args.verbosity)

# Year range logic
if args.fasttest:
    start_year = 2019
    end_year = 2022
    vb.info("⚡ Running in FAST mode (2019–2022)...")
else:
    start_year = 2002
    end_year = 2023



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
    print("Rebalancing portfolio...")
    # final_portfolio = rebalance_portfolio(rdata, factors, start_year=2002, end_year=2023, initial_aum=1)
    final_portfolio = rebalance_portfolio(rdata, factors, start_year=start_year, end_year=end_year, initial_aum=1)

if __name__ == "__main__":
    main()
