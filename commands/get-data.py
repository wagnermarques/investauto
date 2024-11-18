import sys
import os

currDir = os.path.dirname( __file__ )
utilDir = os.path.join( currDir, '..', 'util')
sys.path.append( utilDir )

import Yahoofin
import DbConnection
import Config
import time
import sqlite3

def daemon_process():
    DbConnection.create_database_if_not_exists()
    tickers = Config.TICKETS1
    
    while True:
        stock_prices = Yahoofin.get_stock_prices(tickers)
        DbConnection.save_to_database(stock_prices)
        time.sleep(60)  # wait for 60 seconds before fetching the data again


if __name__ == "__main__":
    daemon_process()
