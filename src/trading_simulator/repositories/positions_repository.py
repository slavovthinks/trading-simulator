from abc import ABC, abstractmethod
from typing import List
from src.trading_simulator.models import Position
from src.trading_simulator.config import get_db_connection

class PositionsRepository(ABC):
    @abstractmethod
    def open_position(self, position: Position):
        ...
    
    @abstractmethod
    def close_position(self, position: Position):
        ...
    
    @abstractmethod
    def get_all_open_positions(self):
        ...
    

class SQLitePositionsRepository(PositionsRepository):
    conn = get_db_connection()

    @classmethod
    def open_position(cls, position: Position):
        ...

    @classmethod
    def close_position(cls, position: Position):
        query = f"""
        UPDATE positions
        SET open=FALSE
        WHERE id={position.id}
        """
        cls.conn.execute(query)

    @classmethod
    def get_all_open_positions(cls) -> List[Position]:
        query = """
            SELECT id, ticker, open_price, open_amount, expires_at
            FROM positions
            WHERE open=TRUE
        """

    
    @classmethod
    def migrate(cls):
        query = """
        CREATE TABLE IF NOT EXISTS positions (
            id INTEGER PRIMARY KEY,
            ticker TEXT,
            open_price REAL,
            open_amount REAL,
            expires_at TIMESTAMP,
            open BOOLEAN
            )
        """
        cls.conn.execute(query)

