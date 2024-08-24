import plotly.graph_objects as go
import plotly.offline as po
import pandas as pd


def get_fig(data_df, patterns=None, candle_opacity=1, line_attr=None, title=''):
    if line_attr is None:
        line_attr = dict(color='deepskyblue', width=2)
    # data_df['date'] = data_df['date'].dt.strftime('%Y/%m/%d %H:%M')
    data = []
    candle_trace = go.Candlestick(
        x=data_df['date'],
        open=data_df['open'],
        high=data_df['high'],
        low=data_df['low'],
        close=data_df['close'],
        name='Candlestick chart',
        opacity=candle_opacity)

    # If patterns are provided, add markers
    if patterns is not None:
        patterns = [date.strftime('%Y-%m-%d %H:%M:%S') for date in patterns['date'].tolist()]
        marker_trace = go.Scatter(
            x=[data_df.loc[data_df['date'] == date, 'date'].values[0] for date in patterns],
            y=[data_df.loc[data_df['date'] == date, 'high'].values[0] for date in patterns],
            mode='markers',
            marker=dict(color='red', size=10),
            name='Pattern Markers'
        )
        data.append(marker_trace)

    data.append(candle_trace)
    fig = go.Figure(data=data)
    fig.update_layout(xaxis_rangeslider_visible=False, title=title)
    fig.update_xaxes(tickangle=45, nticks=20)

    return fig


def fig_plot(fig, filename='PlotFiles/plot.html'):
    po.plot(fig, filename)


def plot(data_df, patterns=None, candle_opacity=1, line_attr=None, title=''):
    fig = get_fig(data_df, patterns, candle_opacity, line_attr, title)
    fig_plot(fig)


if __name__ == '__main__':
    patterns = ['2022-12-20 00:04:00', '2022-12-20 01:35:00']
    df = pd.read_csv('../example-data/EURUSD_Candlestick_Example.csv')
    plot(df, patterns=patterns)
