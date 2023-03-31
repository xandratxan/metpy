# HTML pages of MetPy website

import src.definitions as df
import src.functions as fnc
import src.templates.html.base as bs

# MetPy website index page
index = bs.base_template(
    title='MetPy',
    assets=fnc.html_assets(parent=False),
    header=bs.base_header_template(
        active='index',
        html_index=df.metpy_pages['index'],
        html_projects=df.metpy_pages['projects'],
        html_server=df.metpy_pages['server'],
        html_docs=df.metpy_pages['docs'],
        url_author_github=df.author_xcb['github']
    ),
    main=bs.base_main_template(main='MetPy website index page.'),
    footer=bs.base_footer_template(
        url_author_github=df.author_xcb['github'],
        url_author_email=df.author_xcb['email'],
        url_lmri=df.external_urls['lmri'],
        url_ciemat=df.external_urls['ciemat']
    ),
    scripts=bs.base_scripts_template(assets=fnc.html_assets(parent=False)))

# MetPy website projects page
projects = bs.base_template(
    title='MetPy-Projects',
    assets=fnc.html_assets(parent=False),
    header=bs.base_header_template(
        active='projects',
        html_index=df.metpy_pages['index'],
        html_projects=df.metpy_pages['projects'],
        html_server=df.metpy_pages['server'],
        html_docs=df.metpy_pages['docs'],
        url_author_github=df.author_xcb['github']
    ),
    main=bs.base_main_template(main='MetPy website projects page.'),
    footer=bs.base_footer_template(
        url_author_github=df.author_xcb['github'],
        url_author_email=df.author_xcb['email'],
        url_lmri=df.external_urls['lmri'],
        url_ciemat=df.external_urls['ciemat']
    ),
    scripts=bs.base_scripts_template(assets=fnc.html_assets(parent=False)))

# MetPy website server page
server = bs.base_template(
    title='MetPy-Package Server',
    assets=fnc.html_assets(parent=False),
    header=bs.base_header_template(
        active='server',
        html_index=df.metpy_pages['index'],
        html_projects=df.metpy_pages['projects'],
        html_server=df.metpy_pages['server'],
        html_docs=df.metpy_pages['docs'],
        url_author_github=df.author_xcb['github']
    ),
    main=bs.base_main_template(main='MetPy website server page.'),
    footer=bs.base_footer_template(
        url_author_github=df.author_xcb['github'],
        url_author_email=df.author_xcb['email'],
        url_lmri=df.external_urls['lmri'],
        url_ciemat=df.external_urls['ciemat']
    ),
    scripts=bs.base_scripts_template(assets=fnc.html_assets(parent=False)))

# MetPy website documentation page
documentation = bs.base_template(
    title='MetPy-Documentation',
    assets=fnc.html_assets(parent=False),
    header=bs.base_header_template(
        active='docs',
        html_index=df.metpy_pages['index'],
        html_projects=df.metpy_pages['projects'],
        html_server=df.metpy_pages['server'],
        html_docs=df.metpy_pages['docs'],
        url_author_github=df.author_xcb['github']
    ),
    main=bs.base_main_template(main='MetPy website documentation page.'),
    footer=bs.base_footer_template(
        url_author_github=df.author_xcb['github'],
        url_author_email=df.author_xcb['email'],
        url_lmri=df.external_urls['lmri'],
        url_ciemat=df.external_urls['ciemat']
    ),
    scripts=bs.base_scripts_template(assets=fnc.html_assets(parent=False)))
