# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from ctypes import util
from gettext import install
from .utils import sorted_by_key  # noqa
from floodsystem.stationdata import build_station_list


#Task 1D-1, this function returns the name of rivers with at least one monitoring station in a set
def rivers_with_station(stations):
    rivers = set()
    for i in stations:
        rivers.add(i.river)
    return rivers



# Task 1D-2, this function returns a dictionary with rivers as the key and station objects as the items 
def stations_by_river(stations):
    rivers = (rivers_with_station(stations))
    rivers_dict = {} # Creating empty dictionary
    for i in rivers: # Creating empty lists with the rivers as keys
      rivers_dict[i] = []
    for i in stations:
      rivers_dict[i.river].append(i)
    return rivers_dict



# Task E, this function determines the N rivers with the greatest number of monitoring stations
def rivers_by_station_number(stations, N):
    rivers_dict = stations_by_river(stations)
    rivers_num = [] #Empty list of tuples
    for i in rivers_dict:
        num = len(rivers_dict[i])
        tuple = (i, num) # Creating tuples with river and number of stations on it
        rivers_num.append(tuple) # Adding tuples to the list 
    rivers_num_sorted = sorted(rivers_num, key=lambda tup: tup[1], reverse=True) # Sorted list of tuples in descending order
    rivers_output = rivers_num_sorted[0:N] # Adding the N items to the output

    x = N                              # Checking if the nth item has the same number, if yes add more items until number changes
    while rivers_num_sorted[x][1] == rivers_num_sorted[x-1][1]:
        rivers_output.append(rivers_num_sorted[x])
        x = x +1
    return rivers_output