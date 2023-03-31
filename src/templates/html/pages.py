# HTML pages of MetPy website

import src.definitions as df
import src.functions as fnc
import src.templates.html.base as bs

# Common sections
footer = bs.base_footer_template(
    url_author_github=df.author_xcb['github'],
    url_author_email=df.author_xcb['email'],
    url_lmri=df.external_urls['lmri'],
    url_ciemat=df.external_urls['ciemat']
)

# MetPy website index page
index = bs.base_template(
    title='MetPy',
    assets=fnc.html_assets(parent=False),
    header=bs.base_header_template(active='index'),
    main=bs.base_main_template(main='MetPy website index page.'),
    footer=footer,
    scripts=bs.base_scripts_template(assets=fnc.html_assets(parent=False)))

# MetPy website projects page
projects = bs.base_template(
    title='MetPy-Projects',
    assets=fnc.html_assets(parent=False),
    header=bs.base_header_template(active='projects'),
    main=bs.base_main_template(main='MetPy website projects page.'),
    footer=footer,
    scripts=bs.base_scripts_template(assets=fnc.html_assets(parent=False)))

# MetPy website server page
server = bs.base_template(
    title='MetPy-Package Server',
    assets=fnc.html_assets(parent=False),
    header=bs.base_header_template(active='server'),
    main=bs.base_main_template(main='MetPy website server page.'),
    footer=footer,
    scripts=bs.base_scripts_template(assets=fnc.html_assets(parent=False)))

# MetPy website documentation page
documentation = bs.base_template(
    title='MetPy-Documentation',
    assets=fnc.html_assets(parent=False),
    header=bs.base_header_template(active='docs'),
    main=bs.base_main_template(main='MetPy website documentation page.'),
    footer=footer,
    scripts=bs.base_scripts_template(assets=fnc.html_assets(parent=False)))
