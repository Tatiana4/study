import folium, pandas

vol_table = pandas.read_csv('Volcanoes-USA.txt')
vol_map = folium.Map(location = [vol_table['LAT'].mean(), vol_table['LON'].mean()], zoom_start = 4)

def marker(elev):
    minimum = int(min(vol_table['ELEV']))
    step = int((min(vol_table['ELEV']) + max(vol_table['ELEV'])) / 3)
    if elev in range(minimum, minimum + step):
        color = 'green'
    elif elev in range(minimum + step, minimum + step * 2):
        color = 'blue'
    else:
        color = 'red'
    return color

for lat, lon, name, elev in zip(vol_table['LAT'], vol_table['LON'], vol_table['NAME'], vol_table['ELEV']):
    vol_map.add_child(folium.Marker(location=[lat, lon], popup=name, icon = folium.Icon(color = marker(elev))))

vol_map.save(outfile='test.html')