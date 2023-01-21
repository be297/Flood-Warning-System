from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number

def run():
    """Requirements for Task 1E"""

    # Build list of stations
    stations = build_station_list()

    # Use function to create list when N = 9
    N = 9
    rivers_output=rivers_by_station_number(stations, N)
    print(rivers_output)



if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()








