"""
This script gets KLINE data:
    - History Kline data useful for paper trading
"""



from binance import Client
from env import Key, Secrets

import csv

client = Client(Key, Secrets, testnet=True)

coinPair = "BTCUSDT"

def get_simple_Historical_data():
    candles = client.get_klines(symbol=coinPair, interval=Client.KLINE_INTERVAL_15MINUTE)
    # for candlestick in candles:
    #     print(  "OpenTime :" + str(candlestick[0]) + 
    #         "  Open($) :" + candlestick[1] + 
    #         "  High($) :" + candlestick[2] + 
    #         "  Low($) :" + candlestick[3] + 
    #         "  Close($) :" + candlestick[4]
    #         )
    # csvFile = open('15minutes.csv', 'w', newline='')
    # candlestick_writer = csv.writer(csvFile, delimiter='-')

    # for candlestick in candles:
    #     candlestick_writer.writerow(candlestick)

    with open('15minutes.csv', 'w', newline='') as csvHistory:
        candlestick_writer = csv.writer(csvHistory, delimiter=',')

        for candlestick in candles:
            candlestick_writer.writerow(candlestick)

        csvHistory.close()

# get_simple_Historical_data()


#workable historical data 
def getHitoricalData_csv():

    historyCandles = client.get_historical_klines(coinPair, Client.KLINE_INTERVAL_5MINUTE, "1 Jan, 2012", "28 May, 2021")


    with open('2012to2021.csv', 'w', newline='') as csvHistoryFile:
        candlestick_writer = csv.writer(csvHistoryFile, delimiter=',')

        for candlestick in historyCandles:
            candlestick_writer.writerow(candlestick)

        csvHistoryFile.close()

