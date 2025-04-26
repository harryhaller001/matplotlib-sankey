import os
from datetime import datetime
import sys
from pathlib import Path

DOCS_DIR = Path(__file__).parent
PACKAGE_NAME = "matplotlib-sankey"
PACKAGE_DIR = os.path.abspath("../../matplotlib_sankey")
GITHUB_USER = "harryhaller001"
GITHUB_REPO = "matplotlib-sankey"

sys.path.insert(0, PACKAGE_DIR)

# Project information
project = PACKAGE_NAME
author = GITHUB_USER
copyright = f"{datetime.now():%Y}, {author}."

# Configuration
templates_path = ["_templates"]
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
master_doc = "index"
default_role = "literal"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "nbsphinx",
    "autoapi.extension",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    # Required for syntax highlighing (https://github.com/spatialaudio/nbsphinx/issues/24)
    "IPython.sphinxext.ipython_console_highlighting",
    # Markdown support
    "myst_parser",
]

# Myst parser settings
myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

# Mapping for intersphinx extension
intersphinx_mapping = dict(  # noqa: C408
    numpy=("https://numpy.org/doc/stable/", None),
    matplotlib=("https://matplotlib.org/stable", None),
)

# don't run the notebooks
nbsphinx_execute = "never"

pygments_style = "sphinx"


exclude_trees = ["_build", "dist"]

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]

# Generate the API documentation when building
autoapi_type = "python"
autoapi_add_toctree_entry = False
autoapi_ignore: list[str] = ["_*.py"]
autoapi_dirs = [
    PACKAGE_DIR,
]
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
    "special-members",
    "imported-members",
]
autoapi_member_order = "alphabetical"

autosummary_generate = True

autodoc_member_order = "bysource"
autodoc_typehints = "description"

# Configuration of sphinx.ext.coverage
coverage_show_missing_items = True

# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
napoleon_google_docstring = True
napoleon_attr_annotations = True


# Configurate sphinx rtd theme
html_theme = "sphinx_book_theme"
html_theme_options = dict(  # noqa: C408
    repository_url=f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}",
    repository_branch="main",
    use_download_button=True,
    use_fullscreen_button=False,
    use_repository_button=True,
    # collapse_navbar=False,
)
html_static_path = ["_static"]
html_show_sphinx = False
html_context = dict(  # noqa: C408
    display_github=True,
    github_user=GITHUB_USER,
    github_repo=GITHUB_REPO,
    github_version="main",
    conf_py_path="/docs/",
    github_button=True,
    show_powered_by=False,
)
html_title = PACKAGE_NAME
html_css_files = [
    "css/custom.css",
]
# html_favicon = "./_static/favicon.ico"
