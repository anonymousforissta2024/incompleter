#Source: https://stackoverflow.com/questions/57102028/plotly-attributeerror-figure-object-has-no-attribute-update-layout
from _plotly_future_ import v4_subplots
from plotly.subplots import make_subplots
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.plotly as py

fig1 = make_subplots(
    rows=2, cols=2,
    specs=[[{"type": "pie"}, {"type": "pie"}],
           [{"type": "table"}, {"type": "table"}]],
)

fig1.add_trace(
    go.Pie(
        labels=pie_alarms_total['alarm_type'],
        values=pie_alarms_total['alarm_timestamp'],
        name="Total Alarms",
        title="test"
    ),
    row=1, col=1

)

fig1.add_trace(
    go.Pie(
        labels=pie_alarms_notbd['alarm_type'],
        values=pie_alarms_notbd['alarm_timestamp'],
        name="No TBDs"
    ),
    row=1, col=2
)

fig1.add_trace(
    go.Table(
        header=dict(
            values=pie_alarms_total['alarm_type'],
            line_color='darkslategray',
            fill_color='lightskyblue'
        ),
        cells=dict(
            values=pie_alarms_total['alarm_timestamp'],
            line_color='darkslategray',
            fill_color='lightcyan'
        )
    ),
    row=2, col=1
)

fig1.add_trace(
    go.Table(
        header=dict(
            values=pie_alarms_notbd['alarm_type'],
            line_color='darkslategray',
            fill_color='lightskyblue'
        ),
        cells=dict(
            values=pie_alarms_notbd['alarm_timestamp'],
            line_color='darkslategray',
            fill_color='lightcyan'
        )
    ),
    row=2, col=2
)

fig1.update_layout(title_text="Test")

plot(fig1, filename="test.html")