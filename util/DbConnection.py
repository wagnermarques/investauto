import sqlite3
from sqlite3 import Connection
import time

def create_database_if_not_exists():
    conn = sqlite3.connect('stock_prices.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS stock_prices
                 (timestamp TEXT, ticker TEXT, price REAL)''')
    conn.commit()
    conn.close()


def save_to_database(data):
    conn = sqlite3.connect('stock_prices.db')
    c = conn.cursor()
    for ticker, price in data.items():
        c.execute("INSERT INTO stock_prices (timestamp, ticker, price) VALUES (?, ?, ?)",
                  (time.strftime('%Y-%m-%d %H:%M:%S'), ticker, price))
    conn.commit()
    conn.close()



class ConnectionFactory:
    def __init__(self, db_file: str):
        self.db_file = db_file

    def get_connection(self) -> Connection:
        try:
            conn = sqlite3.connect(self.db_file)
            return conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return None

# Usage example
if __name__ == "__main__":
    factory = ConnectionFactory(Config.DB_SQLITE_FILE)
    connection = factory.get_connection()
    if connection:
        print("Connection established")
        connection.close()