from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

# Print how many rivers have at least one monitoring station and prints the first 10 of these rivers in alphabetical order
stations = build_station_list()
rivers = rivers_with_station(stations)
rivers = sorted(rivers)
print(len(rivers),'stations. The first ten are:', rivers[0:10])



#  Print the names of the stations located on the following rivers in alphabetical order:
rivers_dict = stations_by_river(stations)

# For the River Aire
Aire_list = []
for i in rivers_dict['River Aire']:
  Aire_list.append(i.name)
print(sorted(Aire_list))

# For the River Cam
Cam_list = []
for i in rivers_dict['River Cam']:
  Cam_list.append(i.name)
print(sorted(Cam_list))

# For the River Thames
Thames_list = []
for i in rivers_dict['River Thames']:
  Thames_list.append(i.name)
print(sorted(Thames_list))
   

