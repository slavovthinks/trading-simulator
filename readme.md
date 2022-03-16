# Trading Simulator
Develop a trading simulator to evaluate the quality of a model’s predictions
You are given two 2 inputs:
1. CSV file with the model’s rankings, by date and stock ticker.
1. CSV with the market end-of-day data

The program's result is the portfolio on the last day of trading (according to the market data CSV)

### The logic is as follows:
* Trading is performed on Monday, unless it is a trading holiday so trading will be done on the next trading day. (trading holidays are missing in the market data file).
* Trading means creating a long or short position for a stock (distincted by how many units you buy/sell - positive is buying (long) and negative is selling (short))
* When trading, you have to use all of your cash.
* By the end of a trading day you should have 20 open positions - 10 long and 10 short.
* If a stock is ranked consecutively and it’s position is still open - update it’s trading day.
* Each weekday, positions should be check for settlement by:
    * Stop loss - if it’s losing more than 10% since it’s trading day
    * Take profit - if it’s profiting more than 25% since it’s trading day
    * Expiry time - 14 days have passed since opening it

### Basic assumptions:
* All stocks are US based - so trading holidays are common to all.
* Each position should be settled after 14 days, if it wasn’t settled beforehand.
* In the ranking file - the higher the signal value, the more probability the stock price will increase (long)
* Your portfolio starts with cash only (you’re free to decide how much)
