from matplotlib_sankey._colors import is_color, is_colormap, colormap_to_list


def test_color_utils() -> None:
    """Testing color utils."""
    assert all(
        [
            is_color("blue"),
            is_color("tab:red"),
            is_color("#3456ad"),
            is_color([1, 0.4, 0.2]),
            is_color([255, 60, 60]),
        ]
    )

    assert is_colormap("tab10")
    assert is_colormap("blue") is False

    assert len(colormap_to_list("Reds", 20)) == 20
