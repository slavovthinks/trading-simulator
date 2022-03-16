from abc import ABC, abstractmethod
import datetime

from trading_simulator import models, config

class PredictionsRepostiory(ABC):
    @abstractmethod
    def get_top_predictions(cls, count: int, position_type: models.PositionType, for_date: datetime.datetime):
        pass



class SQLitePredictionsRepository(PredictionsRepostiory):
    conn = config.get_db_connection()

    @classmethod
    def get_top_predictions(cls, count: int, position_type: models.PositionType, for_date: datetime.datetime):
        # Possible issues because of datetime
        date_string = for_date.strftime('%Y-%m-%d')
        order = "ASC" if position_type == models.PositionType.SHORT else "DESC"
        return tuple(
            cls.conn.execute(
                f"""
                SELECT max(date) as date, prediction, ticker
                FROM predictions
                WHERE date(date) <= date('{date_string}')
                GROUP BY ticker
                ORDER BY prediction {order}
                LIMIT {count};
                """
            )
        )
