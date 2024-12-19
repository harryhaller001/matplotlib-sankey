from typing import List, Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.patches import PathPatch, Rectangle
from matplotlib.path import Path
from numpy.typing import NDArray

from ._types import AcceptedColors, CurveType
from ._utils import _clean_axis, _generate_cmap


def sankey_simple(
    data: NDArray,
    colors: AcceptedColors = "tab10",
    spacing: float = 0.0,
    frameon: bool = True,
    figsize: Tuple[int, int] = (5, 5),
    curve_type: CurveType = "curve4",
    alpha: float = 0.5,
    tight_layout: bool = True,
    max_scale: bool = False,
    title: Optional[str] = None,
    column_width: int = 1,
    ribbon_width: int = 12,
) -> Figure:
    """Plot sankey.

    Args:
        data (numpy.ndarray): Input data.
        colors (Union[NDArray, List[str]]): List of colors. Defaults to `tab10`.
        spacing (float, optional): Spacing between column and ribbon patches. Defaults to `0.0`.
        frameon (bool, optional): Draw frame. Defaults to `True`.
        figsize (Tuple[int, int]): Size of figure. Defaults to `(5, 5)`.
        curve_type (Literal["curve3", "curve4", "line"], optional): Curve type ofo ribbon. Defaults to `"curve4"`.
        alpha (float, optional): Alpha of ribbons. Defaults to `0.5`.
        tight_layout (bool, optional): Use tight layout for figure. Defaults to `False`.
        max_scale (bool, optional): Scale values for overall maximum keep absolute differences in column height. Defaults to `False`.
        title (Optional[str], optional): Title of figure. Defaults to `None`.
        column_width (int, optional): Relative width of columns. Defaults to `1`.
        ribbon_width (int, optional): Relative width of ribbons. Defaults to `12`.

    """
    ncols, nrows = data.shape

    # Get cmap
    cmap = _generate_cmap(value=colors, nrows=nrows)

    # Max Scale data to 1
    scaled_data: NDArray[np.float64] = np.zeros(data.shape)
    scale_factor: NDArray[np.float64]

    if max_scale is True:
        scale_factor = np.array([data.sum(axis=1).max()] * ncols)
    else:
        scale_factor = data.sum(axis=1)

    for index, data_colum in enumerate(data):
        scaled_data[index] = data_colum / scale_factor[index]

    assert scaled_data.shape == data.shape, f"Scaled shape {scaled_data.shape} does not match input data {data.shape}"

    # Init figure and axes
    axes: List[Axes]

    fig, axes = plt.subplots(
        nrows=1,
        ncols=ncols + ncols - 1,
        sharey=True,
        width_ratios=[*([column_width, ribbon_width] * (ncols - 1)), column_width],
        frameon=frameon,
        figsize=figsize,
    )

    # Remove spacing
    fig.subplots_adjust(hspace=0, wspace=0)

    total_height = 1.0 + (nrows * spacing)

    # Draw columns on first axes
    axes[0] = _clean_axis(axes[0], frameon=False)
    axes[0].set_ylim(0.0, total_height)

    for index, size in enumerate(scaled_data[0]):
        rect = Rectangle(
            xy=(0, sum(scaled_data[0][:index]) + (index * spacing)), width=1, height=size, color=cmap(index), zorder=1
        )
        axes[0].add_patch(rect)

    for count_index, column_index in enumerate(((np.arange(ncols - 1) + 1) * 2) - 1):
        # Draw ribbons
        axes[column_index] = _clean_axis(axes[column_index], frameon=False)
        axes[column_index].set_ylim(0.0, total_height)

        for index in range(nrows):
            y1_start = sum(scaled_data[count_index][:index])
            y1_end = sum(scaled_data[count_index + 1][:index])

            y2_start = sum(scaled_data[count_index + 1][: index + 1])
            y2_end = sum(scaled_data[count_index][: index + 1])

            poly: PathPatch
            path_patch_kwargs = {
                "color": cmap(index),
                "zorder": 0,
                "alpha": alpha,
                "lw": 0,
            }

            # Add curves
            if curve_type == "curve4":
                poly = PathPatch(
                    Path(
                        vertices=[
                            (0.0, y1_start + (spacing * index)),
                            (0.5, y1_start + (spacing * index)),
                            (0.5, y1_end + (spacing * index)),
                            (1, y1_end + (spacing * index)),
                            (1, y2_start + (spacing * index)),
                            (0.5, y2_start + (spacing * index)),
                            (0.5, y2_end + (spacing * index)),
                            (0, y2_end + (spacing * index)),
                        ],
                        codes=[
                            Path.MOVETO,
                            Path.CURVE4,
                            Path.CURVE4,
                            Path.CURVE4,
                            Path.LINETO,
                            Path.CURVE4,
                            Path.CURVE4,
                            Path.CURVE4,
                        ],
                        closed=True,
                    ),
                    **path_patch_kwargs,
                )

            elif curve_type == "line":
                poly = PathPatch(
                    Path(
                        vertices=[
                            (0, y1_start + (spacing * index)),
                            (1, y1_end + (spacing * index)),
                            (1, y2_start + (spacing * index)),
                            (0, y2_end + (spacing * index)),
                        ],
                        codes=[Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO],
                        closed=True,
                    ),
                    **path_patch_kwargs,
                )

            elif curve_type == "curve3":
                poly = PathPatch(
                    Path(
                        vertices=[
                            (0.0, y1_start + (spacing * index)),
                            (0.5, y1_start + (spacing * index)),
                            (0.5, (y1_start - y1_end) / 2 + y1_end + (spacing * index)),
                            (0.5, y1_end + (spacing * index)),
                            (1, y1_end + (spacing * index)),
                            (1, y2_start + (spacing * index)),
                            (0.5, y2_start + (spacing * index)),
                            (0.5, (y2_start - y2_end) / 2 + y2_end + (spacing * index)),
                            (0.5, y2_end + (spacing * index)),
                            (0, y2_end + (spacing * index)),
                        ],
                        codes=[
                            Path.MOVETO,
                            Path.CURVE3,
                            Path.CURVE3,
                            Path.CURVE3,
                            Path.CURVE3,
                            Path.LINETO,
                            Path.CURVE3,
                            Path.CURVE3,
                            Path.CURVE3,
                            Path.CURVE3,
                        ],
                        closed=True,
                    ),
                    **path_patch_kwargs,
                )
            else:
                raise ValueError(f"curve_type '{curve_type}' not supported.")

            axes[column_index].add_patch(poly)

        # Add column for last data item
        axes[column_index + 1] = _clean_axis(axes[column_index + 1], frameon=False)
        axes[column_index + 1].set_ylim(0.0, total_height)

        for index, size in enumerate(scaled_data[count_index + 1]):
            rect = Rectangle(
                xy=(0, sum(scaled_data[count_index + 1][:index]) + (index * spacing)),
                width=1,
                height=size,
                color=cmap(index),
                zorder=1,
                lw=0,
            )
            axes[column_index + 1].add_patch(rect)

    if title is not None:
        fig.suptitle(title, horizontalalignment="center", verticalalignment="baseline")

    if tight_layout is True:
        fig.tight_layout(pad=0)

    plt.close()
    return fig


def sankey():
    pass
