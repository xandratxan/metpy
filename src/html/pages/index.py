# HTML index pages of MetPy website

import src.definitions as df
import src.functions as fnc
import src.html.templates.base as bs
import src.html.templates.main_section as ms

# Common sections
footer = bs.base_footer_template(
    url_author_github=df.xcb['github'],
    url_author_email=df.xcb['email'],
    url_lmri=df.external_urls['lmri'],
    url_ciemat=df.external_urls['ciemat']
)

# Project cards
packages = {
    'name': 'packages',
    'title': 'Packages',
    'brief_description': 'Packages of the MetPy ecosystem',
    'html_path': df.html_pages['main']['packages'],
    'image_path': fnc.html_images(parent=False),
    'image_name': 'python.png'
}
server = {
    'name': 'server',
    'title': 'Python package server',
    'brief_description': 'Python package server for the MetPy packages',
    'html_path': df.html_pages['main']['server'],
    'image_path': fnc.html_images(parent=False),
    'image_name': 'folder.png'
}
documentation = {
    'name': 'documentation',
    'title': 'Documentation',
    'brief_description': 'Documentation of the MetPy packages',
    'html_path': df.html_pages['main']['docs'],
    'image_path': fnc.html_images(parent=False),
    'image_name': 'python.png'  # TODO: new icon
}

# MetPy website index page
# TODO: cards not showing side by side
metpy_index = bs.base_template(
    title='MetPy',
    assets=fnc.html_assets(parent=False),
    header=bs.base_header_template(active='index'),
    main=bs.base_main_template(main=ms.main_section_template(
        title='Metrology & Python',
        description=(f'MetPy is an ecosystem of Python projects for metrology. '
                     f'It includes a set of Python packages and a PyPI-like package server to provide those packages. '
                     f'Here you can find the packages of the MetPy ecosystem, '
                     f'the server of the MetPy packages and the documentation of the MetPy packages.'),
        cards=[packages, server, documentation])),
    footer=footer,
    scripts=bs.base_scripts_template(assets=fnc.html_assets(parent=False)))
