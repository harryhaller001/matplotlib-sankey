from collections.abc import Sequence

import numpy as np
from matplotlib import colormaps
from matplotlib.axes import Axes
from matplotlib.colors import Colormap, ListedColormap

from ._types import AcceptedColors


def _clean_axis(
    _ax: Axes,
    frameon: bool = True,
    reset_x_ticks: bool = True,
    reset_y_ticks: bool = True,
) -> Axes:
    """Helper function to clean axes."""
    if reset_x_ticks is True:
        _ax.set_xticklabels([])
        _ax.set_xticks([])

    if reset_y_ticks is True:
        _ax.set_yticklabels([])
        _ax.set_yticks([])
        # _ax.set_ylim(0, 1)

    if frameon is False:
        # Despine
        _ax.spines["top"].set_visible(False)
        _ax.spines["left"].set_visible(False)
        _ax.spines["right"].set_visible(False)
        _ax.spines["bottom"].set_visible(False)
    return _ax


def _generate_cmap(value: AcceptedColors, nrows: int) -> Colormap:
    """Util function to generate colormap from list of string or name."""

    def _convert_sequential_cmap_to_listed(c: Colormap, threshold: int = 256) -> Colormap:
        if c.N >= threshold:
            return ListedColormap([c(i) for i in np.linspace(start=0, stop=c.N, num=nrows).astype(int)])

        return c

    if isinstance(value, str):
        # String argument must be the name of an colormap
        assert value in list(colormaps.keys()), f"Value '{value}' is not the name of a valid colormap."

        return _convert_sequential_cmap_to_listed(colormaps.get_cmap(value))

    elif isinstance(value, Sequence):
        return ListedColormap(value)

    elif isinstance(value, Colormap):
        return _convert_sequential_cmap_to_listed(value)

    raise TypeError(f"Type '{type(value).__name__}' not allowed.")
