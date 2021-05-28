"""First I will be using Binance API to get the trading data as a proof of concept for Papertrading.

This system is still in development and Has no algorithm used yet.

IT IS FOR THE BINANCE TESTNET
"""

from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from env import Key, Secrets

client = Client(Key, Secrets, testnet=True)

depth = client.get_order_book(symbol='BNBBTC')

# if you get a timestamp error, restart your time server/sync your clock 
# or see https://github.com/ccxt/ccxt/issues/773#issuecomment-849941742_

#getting your deposit address
btc_deposit_addr = client.get_deposit_address(coin="BTC")
print(btc_deposit_addr["address"])


#getting balance from main account. NOT TESTNET
def privateBalance():
    client = Client(Key, Secrets)
    btc_balance = client.get_asset_balance(asset="BTC")
    print(btc_balance)


privateBalance()