import datetime
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list

# Build list of stations
stations = build_station_list()

# Station name to find
station_name = "Cam"

# Find station
station_cam = None
for station in stations:
    if station.name == station_name:
        station_cam = station
        break
dt = 2
dates, levels = fetch_measure_levels(station_cam.measure_id, dt=datetime.timedelta(days=dt))
print(polyfit(dates, levels, 3))