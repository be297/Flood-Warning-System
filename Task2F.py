import datetime
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    """Requirements for Task 2F"""
    p = 4
     # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    dt=2
    N_list = stations_highest_rel_level(stations, 5)
    for i in N_list:
         dates, levels = fetch_measure_levels(i[0].measure_id, dt=datetime.timedelta(days=dt))
         plot_water_level_with_fit(i[0], dates, levels,p)
    


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()