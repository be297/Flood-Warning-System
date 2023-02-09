





from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    """Requirements for Task 2B"""

 # Build list of stations
stations = build_station_list()
update_water_levels(stations)
tol = 0.8
# Make a descended sorted list of stations above the tolerance and print
tol_list = stations_level_over_threshold(stations, tol)
for i in tol_list:
    print (i[0].name,i[1] )





if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()