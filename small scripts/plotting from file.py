import pandas
from bokeh.plotting import figure, output_file, show

df = pandas.read_csv("plotting from file.csv")
df["Temperature"] = df["Temperature"] / 10
df["Pressure"] = df["Pressure"] / 10

p = figure(plot_width=800, plot_height=800, title="Temperature and Air Pressure")

p.circle(df["Temperature"], df["Pressure"], size=1, color="blue", alpha=0.5)

p.xaxis.axis_label = "Temperature, C"
p.yaxis.axis_label = "Pressure, hPa"

output_file("t_ap.html")
show(p)