from datetime import datetime
from turtle import pos
from typing import Dict, List, Tuple
from src.trading_simulator.models import Position

from trading_simulator import config, models
from trading_simulator.repositories import (
    SQLitePositionsRepository, SQLitePredictionsRepository, SQLiteMarketDataRepository
)


# Create settings with env

class TradeSimulator:
    def __init__(self, start_cash: float = config.START_CASH):
        self.start_cash = start_cash
        self.cash = start_cash
        self.trading_days = self.generate_trading_days()

    def run(self):
        for trading_day in self.trading_days:
            for position in SQLitePositionsRepository.get_all_open_positions():
                position_price = SQLiteMarketDataRepository.get_price(position.ticker, trading_day)
                if self.should_close_position(position, position_price):
                   self.close_position(position)

            if self.cash > 0:
                new_position_size = float(self.cash)/20
                long_predictions = SQLitePredictionsRepository.get_top_predictions(
                    10,
                    models.PositionType.SHORT,
                    trading_day
                )
                short_predictions = SQLitePredictionsRepository.get_top_predictions(
                    10,
                    models.PositionType.LONG,
                    trading_day
                )
                for prediction in (long_predictions + short_predictions):
                    self.open_position(prediction)
        
        print(f"Start cash: {self.start_cash}")
        print(f"End cash: {self.cash}")
    
    def close_position(self, position):
        SQLitePositionsRepository.close_position(position)
        # update available cash

    def should_close_position(self, position: Position, current_price: float) -> bool:
        profit = self.profit_in_percentage(current_price)
        return any(
            (
                profit >= config.TAKE_PROFIT,
                profit <= config.STOP_LOSS,
                position.expires_at <= datetime.now()
            )
        )
        
    def generate_trading_days(self) -> List[datetime.datetime]:
        trading_days = []
        dates = SQLiteMarketDataRepository.get_all_market_dates()
        current_day_index = 0
        while current_day_index <= len(dates) - 1:
            current_day = dates[current_day_index]
            trading_days.append(current_day)
            current_day_index = current_day_index + 5 - current_day.weekday()
        # If first day is not monday remove it from trading days
        if trading_days[0].weekday() != 0:
            trading_days.pop(0)
        return trading_days

# Load csv method for repo class