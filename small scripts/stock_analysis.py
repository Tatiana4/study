from pandas_datareader import data
import datetime
from bokeh.plotting import output_file, show, figure
from bokeh.embed import components
from bokeh.resources import CDN

start = datetime.datetime(2016, 1, 1)
end = datetime.datetime.now()

df = data.DataReader(name="GOOG", data_source="yahoo", start=start, end=end)

def inc_dec(c, o):
    if c > o:
        value = "Increase"
    elif c < o:
        value = "Decrease"
    else:
        value = "Equal"
    return value

df["Status"] = [inc_dec(c, o) for c, o in zip(df.Close, df.Open)]
df["Middle"] = (df.Open + df.Close) / 2
df["Hight"] = abs(df.Open - df.Close)

p = figure(x_axis_type="datetime", height=300, width=1000, title="Candlestick Chart", responsive=True)
p.grid.grid_line_alpha = 0.3

hours_12 = 12 * 3600 * 1000

p.segment(df.index, df.High, df.index, df.Low, color="Black")
p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status == "Increase"], hours_12, df.Hight[df.Status == "Increase"], fill_color="#CCFFFF", line_color="Black")
p.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status == "Decrease"], hours_12, df.Hight[df.Status == "Decrease"], fill_color="#FF3333", line_color="Black")

#script1, div1 = components(p)
#cdn_js = CDN.js_files
#cdn_css = CDN.css_files

output_file("chart.html")
show(p)

