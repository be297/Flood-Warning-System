from floodsystem.stationdata import build_station_list, update_water_levels 
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
from floodsystem.station import inconsistent_typical_range_stations




def stations_level_over_threshold(stations, tol):
    """Task 2B: asses flood risk by level"""
    threshold_list = []
    for i in stations:
        if i.relative_water_level() != None and i.relative_water_level() > tol:
            tuple = (i, i.relative_water_level())
            threshold_list.append(tuple) 
    threshold_list_sorted = sorted(threshold_list, key=lambda tup: tup[1], reverse=True)
    return threshold_list_sorted





def stations_highest_rel_level(stations, N):
    """Task 2C: most at risk stations"""
    high_risk_stations = [] #empty list
    for i in stations:
        if i.relative_water_level() != None:
           tuple = (i, i.relative_water_level())
           high_risk_stations.append(tuple)
    high_risk_stations_sorted = sorted(high_risk_stations, key=lambda tup: tup[1], reverse=True)
    return high_risk_stations_sorted[0:N]

