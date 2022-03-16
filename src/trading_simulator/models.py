from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Optional

import pandas
import src.trading_simulator.config as config


class PositionType(str, Enum):
    SHORT = 'short'
    LONG = 'long'


@dataclass
class Position:
    id: Optional[str]
    ticker: str
    type: PositionType
    open_price: float
    open_amount: float
    expires_at: date  # Should not be aware when it expires all trading logic should be separated

    @property
    def profit_in_percentage(self, current_price: float):
        s = pandas.Series([self.open_price, current_price])
        diff = round(s.pct_change()[1] * 100, 2)
        if self.type == PositionType.SHORT:
            diff = diff * -1
        return diff

    
