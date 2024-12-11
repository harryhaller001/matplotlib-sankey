from matplotlib.axes import Axes


def _clean_axis(_ax: Axes, frameon: bool = True) -> Axes:
    """Helper function to clean axes."""
    _ax.set_yticklabels([])
    _ax.set_xticklabels([])
    _ax.set_ylim(0, 1)
    _ax.set_yticks([])
    _ax.set_xticks([])

    if frameon is False:
        # Despine
        _ax.spines["top"].set_visible(False)
        _ax.spines["left"].set_visible(False)
        _ax.spines["right"].set_visible(False)
        _ax.spines["bottom"].set_visible(False)
    return _ax
