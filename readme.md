# Bindings for trylock/visibility

### Install

First, you need to get pybindgen:

	pip install pybindgen

Then clone and install visibility

	git clone https://gitlab.com/ddorn/visibility/
	cd visibility
	pip install .

### Usage

The whole functionality is in the `VisibiltyCalculator` class.
Initialise it with a list of points and then call `visible_polygon` with
the point of view everu time you want to recalculate a polygon.
This returns a list of points of the polygon.
