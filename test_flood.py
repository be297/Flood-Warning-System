


from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
from floodsystem.station import MonitoringStation


def test_stations_level_over_threshold():
    # Create a station
    s_id = ["test-s-id", "test-b-id", "test-g-id", "test-j-id"]
    m_id = ["test-m-id", "test-m-id2", "test-m-id3","test-m-id4" ]
    label = ["some station", "blah station", "blob station", "haha station"]
    coord = [(-3.0, 4.0), (8.0, 6.0), (12.0,9.0), (5.0, 6.0)]
    trange = [(), (-2, 10), (8,10), (2,4)]
    river = ["River X","River Shaakirah", "River X", "River bonk"]
    town = ["My Town", "East London", "West London", "East Africa"]
    s = MonitoringStation(s_id[0], m_id, label[0], coord[0], trange[0], river[0], town[0])
    b = MonitoringStation(s_id[1], m_id[1], label[1], coord[1], trange[1], river[1], town[1])
    g = MonitoringStation(s_id[2], m_id[2], label[2], coord[2], trange[2], river[2], town[2])
    j = MonitoringStation(s_id[3], m_id[3], label[3], coord[3], trange[3], river[3], town[3])
    s.latest_level = 5.2
    b.latest_level = 6
    g.latest_level = 8
    j.latest_level = 8

    stations=(s,b,g,j)
    tol = 0.5
    tol_list = stations_level_over_threshold(stations, tol)

    assert tol_list[0] == (j, 3)
    assert len(tol_list) == 2


def test_stations_highest_rel_level():
    # Create a station
    s_id = ["test-s-id", "test-b-id", "test-g-id", "test-j-id"]
    m_id = ["test-m-id", "test-m-id2", "test-m-id3","test-m-id4" ]
    label = ["some station", "blah station", "blob station", "haha station"]
    coord = [(-3.0, 4.0), (8.0, 6.0), (12.0,9.0), (5.0, 6.0)]
    trange = [(), (-2, 10), (8,10), (2,4)]
    river = ["River X","River Shaakirah", "River X", "River bonk"]
    town = ["My Town", "East London", "West London", "East Africa"]
    s = MonitoringStation(s_id[0], m_id, label[0], coord[0], trange[0], river[0], town[0])
    b = MonitoringStation(s_id[1], m_id[1], label[1], coord[1], trange[1], river[1], town[1])
    g = MonitoringStation(s_id[2], m_id[2], label[2], coord[2], trange[2], river[2], town[2])
    j = MonitoringStation(s_id[3], m_id[3], label[3], coord[3], trange[3], river[3], town[3])
    s.latest_level = 5.2
    b.latest_level = 6
    g.latest_level = 8
    j.latest_level = 8

    stations=(s,b,g,j)
    N = 2
    N_list = stations_highest_rel_level(stations, N)

    assert N_list[0] == (j, 3)
    assert len(N_list) == 2


