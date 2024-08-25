import plotly.graph_objects as go
import plotly.offline as po

colors = ['red', 'green', 'blue', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']


def get_fig(data_df, patterns=None, candle_opacity=1, title=''):
    data = []
    data_df['date'] = data_df['date'].apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S'))
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
        for i, result in enumerate(patterns):
            pattern = result.get('df')
            pattern = [date.strftime('%Y-%m-%d %H:%M:%S') for date in pattern['date'].tolist()]
            marker_trace = go.Scatter(
                x=[data_df.loc[data_df['date'] == date, 'date'].values[0] for date in pattern],
                y=[data_df.loc[data_df['date'] == date, 'high'].values[0] for date in pattern],
                mode='markers',
                marker=dict(color=colors[(i % len(colors))], size=10),
                name=result.get('name').replace('_', ' ').title()
            )
            data.append(marker_trace)

    data.append(candle_trace)
    fig = go.Figure(data=data)
    fig.update_layout(xaxis_rangeslider_visible=False, title=title)
    fig.update_xaxes(tickangle=45, nticks=20)

    return fig


def fig_plot(fig, filename='PlotFiles/plot.html'):
    po.plot(fig, filename)


def plot(data_df, patterns=None, candle_opacity=1, title=''):
    fig = get_fig(data_df, patterns, candle_opacity, title)
    fig_plot(fig)
