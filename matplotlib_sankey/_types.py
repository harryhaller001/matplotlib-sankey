from collections.abc import Sequence
from typing import Literal, Tuple, TypeAlias, Union

from matplotlib.colors import Colormap

CurveType: TypeAlias = Literal["curve3", "curve4", "line"]

AcceptedColors: TypeAlias = Union[Sequence[str], Colormap, str, Sequence[Tuple[float, float, float]]]
