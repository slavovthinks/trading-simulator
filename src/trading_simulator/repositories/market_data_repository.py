import datetime
from abc import ABC, abstractmethod
from typing import List, Tuple

from trading_simulator import config


class MarketDataRepository(ABC):
    @abstractmethod
    def get_all_market_data(self):
        ...

    @abstractmethod
    def get_price(self, ticker: str, for_date: datetime.datetime):
        ...
    

class SQLiteMarketDataRepository(MarketDataRepository):
    conn = config.get_db_connection()
    
    @classmethod
    def get_all_market_dates(cls) -> Tuple[datetime.datetime]:
        return tuple(datetime.strptime(result[0], "%Y-%m-%d %H:%M:%S") for result in cls.conn.execute("""
            SELECT DISTINCT date
            FROM market_data
            ORDER BY date ASC;
        """).fetchall())
    
    @classmethod
    def get_price(cls, ticker: str, for_date: datetime.datetime):
        date_timestamp = for_date.timestamp()
        query = """
        SELECT price
        FROM market_data
        WHERE date(date) = date({}
        """
        return 
