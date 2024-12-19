from matplotlib import colormaps
from matplotlib.colors import Colormap

from matplotlib_sankey._utils import _generate_cmap


def test_utils_cmap() -> None:
    """Testing utils function to generate cmap."""
    assert isinstance(_generate_cmap("tab10", 4), Colormap)
    assert isinstance(_generate_cmap("viridis", 4), Colormap)
    assert _generate_cmap("viridis", 4).N == 4
    assert isinstance(_generate_cmap(["#ec4899", "#0284c7", "#16a34a", "#f59e0b"], 4), Colormap)
    assert isinstance(_generate_cmap([(0.4, 0.1, 0.9), (0.1, 0.1, 0.7)], 4), Colormap)
    assert isinstance(_generate_cmap(colormaps["tab10"], 4), Colormap)
