from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
from floodsystem.station import inconsistent_typical_range_stations



def run():
    """Requirements for Task 1F"""

 # Build list of stations
stations = build_station_list()

# Build a list of inconsistent stations and print alphabetically
inconsistent_stations = inconsistent_typical_range_stations(stations)  
names = []
for i in inconsistent_stations:
    names.append(i.name)     
print(sorted(names)) 



if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
