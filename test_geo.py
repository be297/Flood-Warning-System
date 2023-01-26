from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.geo import stations_within_radius
from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation
from haversine import haversine 

def test_stations_by_distance():
    # Create a station
    s_id = ["test-s-id", "test-b-id", "test-g-id"]
    m_id = ["test-m-id", "test-m-id2", "test-m-id3"]
    label = ["some station", "blah station", "blob station"]
    coord = [(-3.0, 4.0), (8.0, 6.0), (12.0,9.0)]
    trange = [(), (-1.4, 2.5607), (4.0674,-1.3)]
    river = ["River X","River Shaakirah", "River Hill"]
    town = ["My Town", "East London", "West London"]
    s = MonitoringStation(s_id[0], m_id, label[0], coord[0], trange[0], river[0], town[0])
    b = MonitoringStation(s_id[1], m_id[1], label[1], coord[1], trange[1], river[1], town[1])
    g = MonitoringStation(s_id[2], m_id[2], label[2], coord[2], trange[2], river[2], town[2])

    p = (0,0)

    stations=(s,b,)
    x = stations_by_distance(stations, p)

    assert x[0] == (("some station","My Town"), haversine(coord[0], p))
    assert x[1] == (("blah station","East London"), haversine(coord[1], p))

def test_inconsistent_typical_range_stations():
    # Create a station
    s_id = ["test-s-id", "test-b-id", "test-g-id"]
    m_id = ["test-m-id", "test-m-id2", "test-m-id3"]
    label = ["some station", "blah station", "blob station"]
    coord = [(-3.0, 4.0), (8.0, 6.0), (12.0,9.0)]
    trange = [(), (-1.4, 2.5607), (4.0674,-1.3)]
    river = ["River X","River Shaakirah", "River Hill"]
    town = ["My Town", "East London", "West London"]
    s = MonitoringStation(s_id[0], m_id, label[0], coord[0], trange[0], river[0], town[0])
    b = MonitoringStation(s_id[1], m_id[1], label[1], coord[1], trange[1], river[1], town[1])
    g = MonitoringStation(s_id[2], m_id[2], label[2], coord[2], trange[2], river[2], town[2])

    p = (0,0)

    stations=(s,b,g)
    x = stations_by_distance(stations, p)
    z = inconsistent_typical_range_stations(stations)

    assert z[0] == s
    assert z[1] == g
    assert len(z) == 2

def test_rivers_with_station():
    # Create a station
    s_id = ["test-s-id", "test-b-id", "test-g-id"]
    m_id = ["test-m-id", "test-m-id2", "test-m-id3"]
    label = ["some station", "blah station", "blob station"]
    coord = [(-3.0, 4.0), (8.0, 6.0), (12.0,9.0)]
    trange = [(), (-1.4, 2.5607), (4.0674,-1.3)]
    river = ["River X","River Shaakirah", "River X"]
    town = ["My Town", "East London", "West London"]
    s = MonitoringStation(s_id[0], m_id, label[0], coord[0], trange[0], river[0], town[0])
    b = MonitoringStation(s_id[1], m_id[1], label[1], coord[1], trange[1], river[1], town[1])
    g = MonitoringStation(s_id[2], m_id[2], label[2], coord[2], trange[2], river[2], town[2])

    p = (0,0)
    stations=(s,b,g)
    z = rivers_with_station(stations)
    assert ("River Shaakirah" in z) == True
    assert len(z) == 2
    

    


    



