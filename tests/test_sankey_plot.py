import numpy as np

from matplotlib_sankey import sankey_simple


def test_sankey_simple_plot():
    """Testing simple sankey plot."""
    data = np.array([[10, 24, 50, 80], [14, 30, 24, 40], [4, 10, 50, 53]])
    sankey_simple(data)
