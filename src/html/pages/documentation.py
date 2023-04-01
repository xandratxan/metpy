# HTML documentation pages of MetPy website

import src.definitions as df
import src.functions as fnc
import src.html.templates.base as bs
from src.html.pages.index import footer
import src.html.templates.main_section as ms

# MetPy website documentation page
# TODO: cards not showing side by side
# TODO: add physical-magnitude documentation pages
magnitude = {
    'name': 'magnitude',
    'title': f"{df.magnitude['name']} package",
    'brief_description': df.magnitude['brief_description'],
    'html_path': df.html_pages['docs']['magnitude'],
    'image_path': df.fnc.html_images(parent=False),
    'image_name': df.magnitude['image']
}
metpy_documentation = bs.base_template(
    title='MetPy-Documentation',
    assets=fnc.html_assets(parent=False),
    header=bs.base_header_template(active='docs'),
    main=bs.base_main_template(main=ms.main_section_template(
        title='MetPy Documentation',
        description=(f'MetPy includes a set of Python packages useful for metrology applications. '
                     f'Here you can find the documentation of the MetPy packages.'),
        cards=[magnitude])),
    footer=footer,
    scripts=bs.base_scripts_template(assets=fnc.html_assets(parent=False)))
