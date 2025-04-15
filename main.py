import time
print("main.py reached!", flush=True)

t0 = time.time()

# --- Try imports ---
try:
    from MarketObject import load_data, MarketObject
    from portfolio import Portfolio
    from CalculateHoldings import rebalance_portfolio
    from UserInput import get_factors
    from verbose import log 
    import pandas as pd
    print("All imports successful", flush=True)
except Exception as e:
    print(f"Import error: {e}", flush=True)
    raise

# --- Year selection ---
FASTTEST = True
if FASTTEST:
    start_year = 2019
    end_year = 2022
    log("FASTTEST mode: 2019–2022", level="INFO")
else:
    start_year = 2002
    end_year = 2023
    log("Full simulation: 2002–2023", level="INFO")

# --- Main ---
def main():
    try:
        print("Entering main()", flush=True)
        
        t1 = time.time()
        print("Loading data...", flush=True)
        rdata = load_data()
        print(f"Data loaded in {time.time() - t1:.2f}s", flush=True)

        t2 = time.time()
        print("Preprocessing...", flush=True)
        rdata['Ticker'] = rdata['Ticker-Region'].dropna().apply(lambda x: x.split('-')[0].strip())
        rdata['Year'] = pd.to_datetime(rdata['Date']).dt.year
        print(f"Preprocessing done in {time.time() - t2:.2f}s", flush=True)

        t3 = time.time()
        print("Selecting factors...", flush=True)
        available_factors = ['ROE using 9/30 Data', 'ROA using 9/30 Data', '12-Mo Momentum %', '6-Mo Momentum %', '1-Mo Momentum %', 'Price to Book Using 9/30 Data', 'Next FY Earns/P', '1-Yr Price Vol %', 'Accruals/Assets', 'ROA %', '1-Yr Asset Growth %', '1-Yr CapEX Growth %', 'Book/Price', 'Next-Year\'s Return %', 'Next-Year\'s Active Return %']
        rdata = rdata[['Ticker', 'Ending Price', 'Year'] + available_factors]
        factors = get_factors(available_factors)
        print(f"Got {len(factors)} factors in {time.time() - t3:.2f}s", flush=True)

        t4 = time.time()
        print("Rebalancing portfolio...", flush=True)
        rebalance_portfolio(rdata, factors, start_year, end_year, initial_aum=1)
        print(f"Rebalance done in {time.time() - t4:.2f}s", flush=True)

        print(f"🏁 main() finished in {time.time() - t0:.2f}s", flush=True)

    except Exception as e:
        print(f"Exception inside main: {e}", flush=True)
        raise

if __name__ == "__main__":
    main()
