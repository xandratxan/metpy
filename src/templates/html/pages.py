# HTML pages of MetPy website

import src.definitions as df
import src.functions as fnc
import src.templates.html.base as bs
import src.templates.html.main_section as ms

# Common sections
footer = bs.base_footer_template(
    url_author_github=df.xcb['github'],
    url_author_email=df.xcb['email'],
    url_lmri=df.external_urls['lmri'],
    url_ciemat=df.external_urls['ciemat']
)

# MetPy website index page
index_cards = [df.projects, df.server, df.documentation]
index = bs.base_template(
    title='MetPy',
    assets=fnc.html_assets(parent=False),
    header=bs.base_header_template(active='index'),
    main=bs.base_main_template(main=ms.main_section_template(
        title='Metrology & Python',
        description=(f'MetPy is an ecosystem of Python projects for metrology. '
                     f'It includes a set of Python packages and a PyPI-like package server to provide those packages. '
                     f'Here you can find the projects of the MetPy ecosystem, '
                     f'the server of the MetPy packages and the documentation of the MetPy packages.'),
        cards=index_cards)),
    footer=footer,
    scripts=bs.base_scripts_template(assets=fnc.html_assets(parent=False)))

# MetPy website projects page
project_cards = [df.server, df.magnitude]
projects = bs.base_template(
    title='MetPy-Projects',
    assets=fnc.html_assets(parent=False),
    header=bs.base_header_template(active='projects'),
    main=bs.base_main_template(main=ms.main_section_template(
        title='MetPy Projects',
        description=(f'MetPy includes a set of Python packages useful for metrology applications. '
                     f'MetPy also includes a PyPI-like package server to provide those packages. '
                     f'Here you can find the package server and the packages of the MetPy ecosystem.'),
        cards=project_cards)),
    footer=footer,
    scripts=bs.base_scripts_template(assets=fnc.html_assets(parent=False)))

# MetPy website server page
server_cards = [df.magnitude]
server = bs.base_template(
    title='MetPy-Package Server',
    assets=fnc.html_assets(parent=False),
    header=bs.base_header_template(active='server'),
    main=bs.base_main_template('Package Server page'),
    footer=footer,
    scripts=bs.base_scripts_template(assets=fnc.html_assets(parent=False)))

# MetPy website documentation page
docs_cards = [df.magnitude]
documentation = bs.base_template(
    title='MetPy-Documentation',
    assets=fnc.html_assets(parent=False),
    header=bs.base_header_template(active='docs'),
    main=bs.base_main_template(main=ms.main_section_template(
        title='Documentation page title',  # TODO
        description='Documentation page description',  # TODO
        cards=docs_cards)),
    footer=footer,
    scripts=bs.base_scripts_template(assets=fnc.html_assets(parent=False)))
