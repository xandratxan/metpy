# Package MetPy

> An ecosystem of Python projects for metrology

| **Last version: 0.1.0** | **License: GNU GPL 3.0** | [Source code](https://github.com/xandratxan/metpy/) | [Issues](https://github.com/xandratxan/metpy/issues/) | [Documentation](https://github.com/xandratxan/metpy#readme) |
|-------------------------|--------------------------|-----------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------------|

> **WARNING**: This package is under active development. The current version is considered non-stable.

## MetPy ecosystem

MetPy is an ecosystem of Python projects for metrology. 
It includes:
- A [website](https://xandratxan.github.io/metpy/index.html) at GitHub pages.
- A set of Python packages available at [GitHub](https://xandratxan.github.io/).
- A [PyPI-like package server](https://xandratxan.github.io/metpy/server/index.html) for those packages. 

Packages included in MetPy:
- `physical-magnitude`: [Package](https://xandratxan.github.io/metpy/packages/magnitude.html) for simple operations with magnitudes including units and uncertainties.

## `metpy` repository

The associated `metpy` repository have two functions:
- Build and update the MetPy website on GitHub Pages.
- Build and update the documentation of the MetPy packages using Sphinx.

The MetPy website hosts:
- General information about the MetPy packages.
- A PyPI-like server for the installation of the MetPy packages.
- Documentation of the MetPy packages.

This repository provide:
- HTML templates to build and update the MetPy website.  
- README.md template to build and update the `REAMDE.md` file of the MetPy packages.
- reStructuredText templates to build and update the documentation of the MetPy packages using Sphinx.

File structure and functions:
- `build.py`: Script to build and update the MetPy website and packages documentation.
- `src`: Folder that holds the templates and the scripts to build and update the MetPy website and packages documentation.
- `docs`: Folder that holds the HTML files of the MetPy website and packages documentation to be published in GitHub Pages.
- `build`: Folder not synchronized that holds the HTML files of the MetPy website and packages documentation files to check before publishing.

## Future developments

In the future, MetPy will desirably include packages for:
- Use of calibration radionuclide neutron sources.
- Calibration of neutron dosimeters.
- Unfold neutron spectrum.
- Web application.

## Authors and contributors

Author:
: Xandra Campo,
[@GitHub](https://github.com/xandratxan/)

Contributors:
: Ricardo Gomez,
[@GitHub](https://github.com/ricargoes/)
