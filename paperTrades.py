import ccxt
from env import Key, Secrets

exchange_id = 'binance'



exchange_class = getattr(ccxt, exchange_id) #ccxt.binance.binance

exchange = exchange_class({
    'apiKey': Key,
    'secret': Secrets
})
