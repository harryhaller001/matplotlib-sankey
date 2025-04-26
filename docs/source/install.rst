
.. Licensed under the MIT License
.. _install:


============
Installation
============

.. highlight:: console
.. _setuptools: https://pypi.org/project/setuptools/


For installation of this package you need to have Python 3.10 or newer installed. You can install ``matplotlib-sankey`` with ``pip``::

    pip install matplotlib-sankey


Development
-----------

Install development version of `matplotlib-sankey` with::

    git clone git+https://github.com/harryhaller001/matplotlib-sankey.git


To setup development environment create python virtual environment::

    python3 -m virtualenv venv
    source venv/bin/activate


Use `make` to setup dependencies::

    # Install dependencies and activate pre-commit hook
    make install


Run checks with `make`::

    # Run all checks
    make check

    # Or run individial check functions

    # Run formatting
    make format

    # Run unit testing with pytest
    make testing

    # Run type checks with mypy
    make typing


Dependencies
------------

Required dependencies:

- matplotlib
- numpy
