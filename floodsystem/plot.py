import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

from floodsystem.analysis import polyfit

def plot_water_levels(station, dates, levels):
    """2E - This function returns a graph showing the water levels for a given station in the past days"""
    # Plot
    plt.plot(dates, levels, label = "Water Levels")
    x = np.array([dates[0], dates[-1]])
    y = np.array([station.typical_range[0], station.typical_range[0]])
    plt.plot(x, y, '-g', label = "Typical Low")
    y = np.array([station.typical_range[1], station.typical_range[1]])
    plt.plot(x, y, '-r', label = "Typical High")

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.legend()

    return plt.show()

def plot_water_level_with_fit(station, dates, levels,p):
    poly, d0 = polyfit(dates, levels, p)
    x = matplotlib.dates.date2num(dates)
    
    
