from datetime import datetime

import plotly.graph_objects as go
import pandas as pd

from ubidots_handler.Config import Config
from ubidots_handler.get_data import get_values

conf = Config()


def build_graph():
    df = get_values(device_label=conf.DEVICE_LABEL, var_label=conf.VARIABLE_LABEL,
                                  items=1000000000000000000000000)
    list_date = []
    for dated in df['timestamp']:
        list_date.append(format(datetime.fromtimestamp(dated / 1000).strftime("%H:%M:%S")))
    dates = pd.DataFrame(list_date, columns=['date'])
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates.date, y=df['value'], name="value",
                             line_color='deepskyblue'))

    fig.update_layout(title_text='Time Series with Rangeslider',
                      xaxis_rangeslider_visible=True)

    fig.show()
