from floodsystem.forecast import flood_severity
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 2G"""
     # Build list of stations
    stations = build_station_list()
    Severity_dict = flood_severity(stations)
    none = []
    low = []
    moderate = []
    high = []
    severe = []
    for i in Severity_dict:
        x = (Severity_dict.get(i))
        if x == "Not enough data":
            none.append(i)
        elif x == "Low":
            low.append(i)
        elif x == "Moderate":
            moderate.append(i)
        elif x == "High":
            high.append(i)
        else:
            severe.append(i)
    print("These stations do not have enough data", none)
    print("These stations are low", low)
    print("These stations are moderate", moderate)
    print("These stations are high", high)
    print("These stations are severe", severe)


 
    
if __name__ == "_main_":
    print("* Task 2G: CUED Part IA Flood Warning System *")
    run()