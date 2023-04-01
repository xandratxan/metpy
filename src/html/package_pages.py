# HTML package pages of MetPy website

import src.functions as fnc
import src.html.templates.base as bs
from src.html.main_pages import footer

# HTML physical-magnitude package page
magnitude = bs.base_template(
    title='MetPy-Packages-Physical-magnitude',
    assets=fnc.html_assets(parent=True),
    header=bs.base_header_template(active='projects'),
    main=bs.base_main_template(main='MetPy Packages: physical-magnitude package page'),
    footer=footer,
    scripts=bs.base_scripts_template(assets=fnc.html_assets(parent=False)))
