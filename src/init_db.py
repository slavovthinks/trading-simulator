import pandas
from src.trading_simulator.config import get_db_connection




conn = get_db_connection()
parse_dates = ['date']
df = pandas.read_csv("./market_data.csv", parse_dates=parse_dates)
df.to_sql("market_data", conn, if_exists='append', index=False)
df = pandas.read_csv("./predictions.csv", parse_dates=parse_dates)
df.to_sql("predictions", conn, if_exists='append', index=False)


