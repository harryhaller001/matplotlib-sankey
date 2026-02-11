matplotlib_sankey
=================

.. py:module:: matplotlib_sankey


Attributes
----------

.. autoapisummary::

   matplotlib_sankey.__version__


Functions
---------

.. autoapisummary::

   matplotlib_sankey.from_matrix
   matplotlib_sankey.sankey


Package Contents
----------------

.. py:data:: __version__
   :value: '0.3.1'


.. py:function:: from_matrix(mtx, source_indicies = None, target_indicies = None)

   Convert weight matrix to tuple of source, target and weight.

   :param mtx: Weight matrix (source x target).
   :type mtx: Sequence[Sequence[int | float]], optional
   :param source_indicies: List of source indices. Defaults to `None`.
   :type source_indicies: list[int | str] | None, optional
   :param target_indicies: List of target indices. Defaults to `None`.
   :type target_indicies: list[int | str] | None, optional

   :returns: List of tuples containing source, target and weight.

   ReturnType:
       list[tuple[int | str, int | str, float | int]]



.. py:function:: sankey(data, figsize = None, frameon = False, ax = None, spacing = 0.0, annotate_columns = None, rel_column_width = 0.15, color = 'tab10', curve_type = 'curve4', ribbon_alpha = 0.2, ribbon_color = 'black', title = None, show = True, show_legend = False, legend_labels = None, column_labels = None, annotate_columns_font_kwargs = None, annotate_columns_font_color = 'auto')

   Sankey plot.

   :param data: Input data.
   :type data: list[list[tuple[int | str, int | str, float | int]]]
   :param figsize: Size of figure. Defaults to `None`.
   :type figsize: tuple[int, int] | None
   :param frameon: Draw frame. Defaults to `True`.
   :type frameon: bool, optional
   :param ax: Provide matplotlib Axes instance for plotting. Defaults to `None`.
   :type ax: matplotlib.Axes | None, optional
   :param spacing: Spacing between column and ribbon patches. Defaults to `0.0`.
   :type spacing: float, optional
   :param annotate_columns: Annotate columns of plot. Annotations options are column name (`index`), column total weight (`weight`) or percent of weight (`weight_percent`). Defaults to `None`.
   :type annotate_columns: Literal["index", "weight", "weight_percent"], optional
   :param rel_column_width: Relative width of columns compared to ribbons. Defaults to `0.15`. Value must be between 0 and 1.
   :type rel_column_width: float, optional
   :param color: Colors or colormap for columns.
   :type color: Sequence[str] | Colormap | str | Sequence[tuple[float, float, float]], optional
   :param curve_type: Curve type ofo ribbon. Defaults to `"curve4"`.
   :type curve_type: Literal["curve3", "curve4", "line"], optional
   :param ribbon_alpha: Alpha of ribbons. Defaults to `0.2`.
   :type ribbon_alpha: float, optional
   :param ribbon_color: Color of ribbons. Defaults to `"black"`.
   :type ribbon_color: str, optional
   :param title: Title of figure. Defaults to `None`.
   :type title: str | None, optional
   :param show: Show figure. Defaults to `True`.
   :type show: bool, optional
   :param show_legend: Show legend. Defaults to `False`. If legend should be displayed, also provide `legend_labels`.
   :type show_legend: bool, optional
   :param legend_labels: Labels to display in legend. Defaults to `None`.
   :type legend_labels: list[str] | None, optional
   :param column_labels: Labels for columns. Defaults to `None`.
   :type column_labels: list[str] | None, optional
   :param annotate_columns_font_kwargs: Extra arguments for column `ax.text` method of column annotation. Defaults to `None`.
   :type annotate_columns_font_kwargs: dict[str, Any] | None, optional
   :param annotate_columns_font_color: Color of column annotation text. Defaults to `"auto"`, thereby automatically selectes text color based on background color.
   :type annotate_columns_font_color: Literal["auto"] | ColorTuple | str, optional

   :returns: Matplotlib axes instance.

   ReturnType:
       matplitlib.Axes
