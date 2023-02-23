import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):
    """Task 2F: function fitting"""
    x = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(x, levels, p)
    poly = np.poly1d(p_coeff)
    return poly, d0