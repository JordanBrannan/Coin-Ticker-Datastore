import ccxt
import time

from arctic import Arctic
import pandas as pd
import pymongo


# Exchange + Pair
def monitor_pair(pairs, exchange, store):

    library = store[exchange.upper()]
    exchange_class = getattr(ccxt, exchange.lower())
    exchange = exchange_class({})

    while True:
        # Load ticker info
        if (exchange.has['fetchTicker']):
            # Iterate through each symbol in pairs list
            for symbol in pairs:
                # Get ask/bid/last etc.
                data = exchange.fetch_ticker(symbol)

                # Append to database
                srs_data = pd.Series(data)[['bid', 'ask', 'last']].astype(float)
                time_data = pd.datetime.fromtimestamp(int(data['timestamp'] / 1000))
                df_data = pd.DataFrame([srs_data], index=[time_data])
                library.append(symbol, df_data)

                item = library.read(symbol) # For debug
                testData = item.data # For debug
                print(testData) # For debug
            #break # For debug
            time.sleep(30)