from dataclasses import dataclass

import yfinance as yf


@dataclass
class StockData:
    """A data class representing stock data.

    Args:
        ticker: The stock ticker symbol.

    Returns:
        None

    Examples:
        stock = StockData(ticker='AAPL')
    """

    tickers: str | list[str]

    def single_company_history(
        self, start=None, end=None, period="Max", interval="1d", **kwargs
    ):
        self.history_data = yf.download(
            tickers=self.tickers,
            start=start,
            end=end,
            period=period,
            interval=interval,
            group_by="ticker",
            rounding=True,
            **kwargs,
        )

        return self

    def filter_company(self, ticker: str):
        self.history_data = self.history_data[ticker]
        return self
