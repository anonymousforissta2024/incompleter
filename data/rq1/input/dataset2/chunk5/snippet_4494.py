#Source: https://stackoverflow.com/questions/57302078/constant-name-errors-in-ipython
df["date"] = pd.to_datetime(df.index)

mids = (df.Open + df.Close)/2
spans = abs(df.Close-df.Open)

inc = df.Close > df.Open
dec = df.Open > df.Close
w = 12*60*60*1000 # half day in ms

output_notebook()

TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000,      toolbar_location="left",y_axis_label = "Price",
      x_axis_label = "Date")

p.segment(df.date, df.High, df.date, df.Low, color="black")
p.rect(df.date[inc], mids[inc], w, spans[inc], fill_color='green', line_color="green")
p.rect(df.date[dec], mids[dec], w, spans[dec], fill_color='red', line_color="red")
p.line(df.date,state_means,line_width=1,line_color = 'blue',legend="Kalman filter")

p.title = "Implementation of Kalman Filter Estimation - TCS EOD chart"
p.xaxis.major_label_orientation = pi/4
p.grid.grid_line_alpha=0.3