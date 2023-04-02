"""HTML documentation pages of MetPy website."""

import src.definitions as df
import src.html.templates.base as bs
import src.html.templates.main_section as ms
from src.html.pages.index import footer

# MetPy website documentation page
# TODO: cards not showing side by side
# TODO: add physical-magnitude documentation pages
magnitude = {
    'name': 'magnitude',
    'title': f"{df.magnitude['name']} package",
    'brief_description': df.magnitude['brief_description'],
    'html_path': df.html_pages['documentation']['magnitude'],
    'image': df.magnitude['image']
}
metpy_documentation = bs.base_template(
    title='MetPy-Documentation',
    header=bs.base_header_template(active='docs'),
    main=bs.base_main_template(
        main=ms.main_section_template(
            title='MetPy Documentation',
            description=(f'MetPy includes a set of Python packages useful for metrology applications. '
                         f'Here you can find the documentation of the MetPy packages.'),
            image='documents.png',
            cards=[magnitude]
        )
    ),
    footer=footer,
    scripts=bs.base_scripts_template()
)
