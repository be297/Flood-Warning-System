from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    """Requirements for Task 2C"""

     # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    N_list = stations_highest_rel_level(stations, 10)
    

    for i in N_list:
        print (i[0].name, i[1])

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
