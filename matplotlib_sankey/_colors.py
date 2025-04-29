from typing import Any
import re
from matplotlib.colors import get_named_colors_mapping, Normalize

from ._utils import isinstance_list_of

from matplotlib import colormaps


def is_colormap(name: str) -> bool:
    """Check if string is name of valid colormap."""
    return name in colormaps.keys()


def is_hex_color(color: Any) -> bool:
    """Check of object is hex color string.

    Args:
        color (typing.Any): Object to check.

    Returns: boolean.

    ReturnType: bool

    """
    if isinstance(color, str):
        return re.match(r"^\#([a-f0-9A-F]{6})$", color) is not None
    return False


def is_color(color: Any) -> bool:
    """Check if value is a valid color."""
    if isinstance(color, str):
        # Check if value is hex string
        if is_hex_color(color):
            return True

        # Check if value is named color
        return color in get_named_colors_mapping().keys()
    elif isinstance(color, list | tuple | set):
        # Check if value is list|tuple of int|float
        color = list(color)

        # if len(color) == 3 or len(color) == 4:
        if len(color) == 3:
            return isinstance_list_of(color, int | float)

    return False


def colormap_to_list(
    name: str,
    num: int | None = None,
    rollover: bool = True,
    norm_vmin: int = 0,
) -> list[tuple[float, ...]]:
    """Generate list of color tuples from cmap name."""
    assert is_colormap(name)

    cmap = colormaps.get_cmap(name)

    max_iter = cmap.N

    if num is not None:
        max_iter = num

    norm = Normalize(vmin=norm_vmin, vmax=cmap.N)

    if cmap.N == 256:
        # Norm sequencial colors
        norm = Normalize(vmin=norm_vmin, vmax=max_iter % cmap.N)

    if rollover is True:
        return [tuple(float(c) for c in cmap(norm(i % cmap.N))[:3]) for i in range(max_iter)]
    return [tuple(float(c) for c in cmap(norm(i))[:3]) for i in range(max_iter)]
