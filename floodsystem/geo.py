# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

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
