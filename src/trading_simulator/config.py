import sqlite3

STOP_LOSS = float(-10)
TAKE_PROFIT = float(25)
START_CASH = float(10000)
DB_PATH = 'simulator.db'


def get_db_connection():
    return sqlite3.connect(DB_PATH)
