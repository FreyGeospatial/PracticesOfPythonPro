import plotly.graph_objects as go

trace1 = go.Scatter(
    x=[1,2,3],
    y=[4,5,6],
    marker={'color': 'red', 'symbol': 104},
    mode='markers+lines',
    text=['one', 'two', 'three'],
    name='1st Trace',
)

trace1 = go.Scatter()
trace1.set_x_data([1,2,3])
trace1.set_y_data([4,5,6])
trace1.set_marker_config({'color':'red', 'symbol':104, 'size':10})
trace1.set_mode('markers_lines')