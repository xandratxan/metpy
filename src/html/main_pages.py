# HTML pages of MetPy website

import src.definitions as df
import src.functions as fnc
import src.html.templates.base as bs
import src.html.templates.main_section as ms

# TODO: cards not showing side by side

# Common sections
footer = bs.base_footer_template(
    url_author_github=df.xcb['github'],
    url_author_email=df.xcb['email'],
    url_lmri=df.external_urls['lmri'],
    url_ciemat=df.external_urls['ciemat']
)

# Project cards
index_cards = [df.packages, df.server, df.documentation]
package_cards = [df.magnitude]

# MetPy website index page
index = bs.base_template(
    title='MetPy',
    assets=fnc.html_assets(parent=False),
    header=bs.base_header_template(active='index'),
    main=bs.base_main_template(main=ms.main_section_template(
        title='Metrology & Python',
        description=(f'MetPy is an ecosystem of Python projects for metrology. '
                     f'It includes a set of Python packages and a PyPI-like package server to provide those packages. '
                     f'Here you can find the packages of the MetPy ecosystem, '
                     f'the server of the MetPy packages and the documentation of the MetPy packages.'),
        cards=index_cards)),
    footer=footer,
    scripts=bs.base_scripts_template(assets=fnc.html_assets(parent=False)))

# MetPy website packages page
# TODO: add link to physical-magnitude package page
# TODO: add physical-magnitude package page
projects = bs.base_template(
    title='MetPy-Packages',
    assets=fnc.html_assets(parent=False),
    header=bs.base_header_template(active='projects'),
    main=bs.base_main_template(main=ms.main_section_template(
        title='MetPy Packages',
        description=(f'MetPy includes a set of Python packages useful for metrology applications. '
                     f'Here you can find the packages of the MetPy ecosystem.'),
        cards=package_cards)),
    footer=footer,
    scripts=bs.base_scripts_template(assets=fnc.html_assets(parent=False)))

# MetPy website server page
# TODO: add server main page
# TODO: add server physical-magnitude page
# TODO: test server functionality
server_cards = [df.magnitude]
server = bs.base_template(
    title='MetPy-Package Server',
    assets=fnc.html_assets(parent=False),
    header=bs.base_header_template(active='server'),
    main=bs.base_main_template((f'MetPy includes a PyPI-like package server to provide the MetPay packages. '
                                f'Here you can find the package server.')),
    footer=footer,
    scripts=bs.base_scripts_template(assets=fnc.html_assets(parent=False)))

# MetPy website documentation page
# TODO: add link to physical-magnitude documentation pages
# TODO: add physical-magnitude documentation pages
docs_cards = [df.magnitude]
documentation = bs.base_template(
    title='MetPy-Documentation',
    assets=fnc.html_assets(parent=False),
    header=bs.base_header_template(active='docs'),
    main=bs.base_main_template(main=ms.main_section_template(
        title='MetPy Documentation',
        description=(f'MetPy includes a set of Python packages useful for metrology applications. '
                     f'Here you can find the documentation of the MetPy packages.'),
        cards=package_cards)),
    footer=footer,
    scripts=bs.base_scripts_template(assets=fnc.html_assets(parent=False)))