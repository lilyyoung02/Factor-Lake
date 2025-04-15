import time
print("✅ main.py reached!", flush=True)
time.sleep(1)

from MarketObject import load_data, MarketObject
from portfolio import Portfolio
from CalculateHoldings import rebalance_portfolio
from UserInput import get_factors
from verbose import log 
import pandas as pd

# Year range logic (hardcoded for now — optional to toggle fasttest inside Colab)
FASTTEST = True

if FASTTEST:
    start_year = 2019
    end_year = 2022
    log("⚡ Running in FAST mode (2019–2022)...", level="INFO")
else:
    start_year = 2002
    end_year = 2023
    log("🏁 Running full simulation (2002–2023)...", level="INFO")

def main():
    print("✅ main() started", flush=True)
    for i in range(5):
        print(f"Simulating step {i}...", flush=True)
        time.sleep(1)
    # ### Load market data ###
    # start = time.time()
    # print("Loading market data...")
    # rdata = load_data()
    # log(f"load_data() took {time.time() - start:.2f}s", level="INFO")

    # ### Data preprocessing ###
    # print("Processing market data...")
    # rdata['Ticker'] = rdata['Ticker-Region'].dropna().apply(lambda x: x.split('-')[0].strip())
    # rdata['Year'] = pd.to_datetime(rdata['Date']).dt.year
    # available_factors = ['ROE using 9/30 Data', 'ROA using 9/30 Data', '12-Mo Momentum %', '6-Mo Momentum %', '1-Mo Momentum %', 'Price to Book Using 9/30 Data', 'Next FY Earns/P', '1-Yr Price Vol %', 'Accruals/Assets', 'ROA %', '1-Yr Asset Growth %', '1-Yr CapEX Growth %', 'Book/Price', 'Next-Year\'s Return %', 'Next-Year\'s Active Return %']
    # rdata = rdata[['Ticker', 'Ending Price', 'Year'] + available_factors]
    # factors = get_factors(available_factors)

    # ### Rebalancing portfolio across years ###
    # print("Rebalancing portfolio...")
    # # final_portfolio = rebalance_portfolio(rdata, factors, start_year=2002, end_year=2023, initial_aum=1)
    # final_portfolio = rebalance_portfolio(rdata, factors, start_year=2019, end_year=2021, initial_aum=1)

    # print("🟩 Script reached end of main()", flush=True)


if __name__ == "__main__":
    main()
