from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """Requirements for Task 1B"""

    #Build list of stations
    stations = build_station_list()   

    #define p
    p = (52.2053, 0.1218)
   
    print('The closest 10 stations are', stations_by_distance(stations, p)[:10])

    print('The furthest 10 stations are', stations_by_distance(stations, p)[-10:]) 


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()

    