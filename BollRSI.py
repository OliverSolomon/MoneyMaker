import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("2012to2021.csv")


# df = df.set_index(pd.DatetimeIndex(df[0].values))
df = df.set_index(df['OpenTime'].values)

figure = go.Figure(
    data = [
        go.Candlestick(
            x = df['OpenTime'],
            low = df['Low'],
            high = df['High'],
            close = df['Close'],
            open = df['Open'],
            increasing_line_color = 'green',
            decreasing_line_color = 'red'

        )
    ]
)

figure.show()


def short():
    RSI = "RSI generated"