import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):
    """Task 2F: function fitting"""
    x = matplotlib.dates.date2num(dates)
    d0 = x[0]
    p_coeff = np.polyfit(x-d0, levels, p)
    poly = np.poly1d(p_coeff)
    return poly, d0