# HTML server pages of MetPy website

import src.functions as fnc
import src.html.templates.base as bs
from src.html.pages.index import footer

# MetPy website server page
# TODO: add server main page
# TODO: add server physical-magnitude page
# TODO: test server functionality
metpy_server = bs.base_template(
    title='MetPy-Package Server',
    assets=fnc.html_assets(parent=False),
    header=bs.base_header_template(active='server'),
    main=bs.base_main_template((f'MetPy includes a PyPI-like package server to provide the MetPay packages. '
                                f'Here you can find the package server.')),
    footer=footer,
    scripts=bs.base_scripts_template(assets=fnc.html_assets(parent=False)))

# MetPy server packages, physical-magnitude package page
