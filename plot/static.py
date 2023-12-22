from data.download import download_data
from plotnine import (
    ggplot, aes,
    geom_line, ggtitle,
    xlab,ylab
)


def plot_nine(ticker:str) -> ggplot:
    """flat a static plot usinbg plotline

    Args:
        ticker (str): the ticker of financial asset.

    Returns:
        ggplot: A line chart depicting the historical closing prices.
    """

    data = download_data(ticker)

    fig = ggplot (
    data = data.reset_index(),
    mapping = aes( x = "Date", y = "Close")
   ) +\
    geom_line() +\
    ggtitle("Dados históricos do {ticker}:") +\
    xlab("Data") +\
    ylab("Fechamento")  

    return fig
\


