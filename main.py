"""First I will be using Binance API to get the trading data as a proof of concept for Papertrading.

This system is still in development and Has no algorithm used yet.

IT IS FOR THE BINANCE TESTNET
"""

from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from env import Key, Secrets


from historyDataGetter import get_simple_Historical_data, getHitoricalData_csv

client = Client(Key, Secrets, testnet=True)

coinPair = "BTCUSDT"

depth = client.get_order_book(symbol=coinPair)

# if you get a timestamp error, restart your time server/sync your clock 
# or see https://github.com/ccxt/ccxt/issues/773#issuecomment-849941742_
# for linux systems run "sudo systemctl restart ntp "

#getting your deposit address
btc_deposit_addr = client.get_deposit_address(coin="BTC")
print(btc_deposit_addr["address"])


#getting balance from main account. NOT TESTNET
def privateBalance():
    client = Client(Key, Secrets)
    btc_balance = client.get_asset_balance(asset="BTC")
    print(btc_balance)

privateBalance()


#show current prices of all alts on binance
def balances():
    alts_prices = client.get_all_tickers()
    
    for token in alts_prices:
        print(token["symbol"] + " : " + token["price"])

balances()



#Get KLines. 

#klines for BTCUSDT for 15 minutes.
get_simple_Historical_data()

#get workable KLINE data. (1, Jan 2012 - 28, May 2021)
# getHitoricalData_csv()

# Plot KLINES using Matplotlib or ploty
