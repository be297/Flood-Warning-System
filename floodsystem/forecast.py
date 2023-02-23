import datetime
import matplotlib
import matplotlib.dates as mdates
import numpy as np
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import update_water_levels


def flood_severity(stations):
    update_water_levels(stations)
    Severity_dict = {}
    tol = 1.5
    # Dealing with cases where there is not enough data to make a valuable decision
    inconsistent_stations = inconsistent_typical_range_stations(stations)  
    for i in inconsistent_stations:
        Severity_dict[i.name] = "Not enough data"
    for i in stations:
        if i.latest_level == None:
            Severity_dict[i.name] = "Not enough data"
    
    # Dealing with severe cases (if tol is above 1.5)
    tol_list = stations_level_over_threshold(stations, tol)
    for i in tol_list:
        Severity_dict[i[0].name] = "Severe"

    # Dealing with low cases
    for i in stations:
        if i.name not in Severity_dict.keys():
            if i.relative_water_level() < 0.75:
                Severity_dict[i.name] = "Low"
    
    # Dealing with moderate and high cases
    tol = 0.75
    dt = 10
    tol_list = stations_level_over_threshold(stations, tol)
    for i in tol_list:
        if i[0].name not in Severity_dict.keys():
            dates, levels = fetch_measure_levels(i[0].measure_id, dt=datetime.timedelta(days=dt))
            x = matplotlib.dates.date2num(dates)
            array = np.array(x)
            array = array - x[0]
            if ((levels[-1]-levels[-6])/(x[-1]-x[-6])) > 0:
                Severity_dict[i[0].name] = "High"
            else:
                Severity_dict[i[0].name] = "Moderate"
    return Severity_dict





        


    
    


