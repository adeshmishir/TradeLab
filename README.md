# TradeLab

TradeLab is a quantitative trading research platform built in Python for designing, testing, and evaluating algorithmic trading strategies on historical market data.

The project allows traders and researchers to backtest strategies, analyze performance metrics, and compare different approaches before deploying capital in live markets.

## Features

* Historical market data backtesting
* Moving Average Crossover strategy
* RSI-based trading strategy
* Momentum strategy
* Performance analytics and reporting
* Sharpe Ratio calculation
* Sortino Ratio calculation
* Maximum Drawdown analysis
* CAGR and annualized return metrics
* Trade history and portfolio statistics
* Interactive equity curve visualization

## Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Backtesting.py
* Yahoo Finance (yfinance)

## Project Structure

```text
TradeLab/
├── strategies/
│   ├── sma.py
│   ├── rsi.py
│   └── momentum.py
├── data/
├── results/
├── main.py
├── requirements.txt
└── README.md
```

## Example Strategy

```python
from backtesting import Backtest, Strategy

class SmaCross(Strategy):
    def init(self):
        pass

    def next(self):
        pass
```

## Metrics Generated

* Total Return
* Annualized Return
* CAGR
* Sharpe Ratio
* Sortino Ratio
* Profit Factor
* Win Rate
* Maximum Drawdown
* Trade Statistics

## Future Improvements

* Portfolio backtesting
* Multi-asset strategy support
* Strategy optimization engine
* Streamlit dashboard
* Live market data integration
* Paper trading module

## Installation

```bash
git clone https://github.com/adeshmishir/TradeLab.git
cd TradeLab

python -m venv .venv
source .venv/Scripts/activate

pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Author

Adesh Mishra
