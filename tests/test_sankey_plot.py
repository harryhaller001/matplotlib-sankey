import matplotlib.pyplot as plt
import pytest

from matplotlib_sankey import sankey


def test_sankey_simple_plot():
    """Testing simple sankey plot."""
    data = [
        [(0, 2, 20), (0, 1, 10), (3, 4, 15), (3, 2, 10), (5, 1, 5), (5, 2, 50)],
        [(2, 6, 40), (1, 6, 15), (2, 7, 40), (4, 6, 15)],
        [(7, 8, 5), (7, 9, 5), (7, 10, 20), (7, 11, 10), (6, 11, 55), (6, 8, 15)],
    ]
    sankey(data, frameon=True)
    sankey(data, curve_type="curve3")
    sankey(data, curve_type="line")
    sankey(data, title="test", annotate_columns="index")
    sankey(data, color="Reds", annotate_columns="weight")
    sankey(data, color="tab:red", annotate_columns="weight_percent", annotate_columns_font_color="white")
    sankey(data, color=["tab:red", "Reds", (0.1, 0.4, 1.0), "viridis"])
    sankey(data, show_legend=True)
    sankey(data, color="tab:red", column_labels=["A", "B", "C", "D"], show=False)

    _, ax = plt.subplots()
    sankey(data, ax=ax)


def test_sankey_column_item_totals():
    """Testing sankey plot with column_item_totals."""
    data = [
        [(0, 1, 30), (0, 2, 20), (3, 1, 15), (3, 2, 25)],
        [(1, 4, 40), (2, 4, 30), (2, 5, 15)],
    ]

    # Test with valid totals (larger than ribbon sums)
    column_item_totals = [
        {0: 60, 3: 50},  # Column 0
        {1: 60, 2: 60},  # Column 1
        {4: 90, 5: 25},  # Column 2
    ]

    ax = sankey(
        data=data,
        column_item_totals=column_item_totals,
        annotate_columns="weight",
        show=False,
    )
    assert ax is not None

    # Test with totals equal to ribbon sums (should work)
    column_item_totals_equal = [
        {0: 50, 3: 40},
        {1: 45, 2: 45},
        {4: 70, 5: 15},
    ]

    ax = sankey(
        data=data,
        column_item_totals=column_item_totals_equal,
        show=False,
    )
    assert ax is not None


def test_sankey_column_item_totals_validation():
    """Testing validation of column_item_totals parameter."""
    data = [
        [(0, 1, 30), (0, 2, 20)],
    ]

    # Test with wrong number of columns
    with pytest.raises(AssertionError, match="must have 2 entries"):
        sankey(
            data=data,
            column_item_totals=[{0: 50}],  # Only 1 column, should be 2
            show=False,
        )

    # Test with missing item in totals
    with pytest.raises(ValueError, match="has ribbons but no total value provided"):
        sankey(
            data=data,
            column_item_totals=[{0: 50}, {1: 50}],  # Missing item 2 in column 1
            show=False,
        )

    # Test with total less than ribbon sum
    with pytest.raises(ValueError, match="is less than sum of ribbon weights"):
        sankey(
            data=data,
            column_item_totals=[
                {0: 40},  # Total 40 < ribbon sum 50
                {1: 30, 2: 20},
            ],
            show=False,
        )
