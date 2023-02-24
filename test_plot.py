import pytest

from floodsystem.plot import plot_water_levels
station = "x"
dates = 5


def test_plot_water_levels():
    with pytest.raises(ValueError):
        plot_water_levels(station, dates)
