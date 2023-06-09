"""HTML documentation pages of MetPy website."""

import src.definitions as df
import src.html.templates.base as bs
import src.html.templates.main_section as ms

# MetPy website documentation page
magnitude = {
    'name': 'magnitude',
    'title': f"Physical magnitude documentation",
    'brief_description': df.magnitude['brief_description'],
    'html_path': df.html_pages['documentation']['magnitude'],
    'image': df.magnitude['image']
}
documentation = bs.base_template(
    title='MetPy-Documentation',
    header=bs.base_header_template(active='docs'),
    main=bs.base_main_template(
        main=ms.main_section_template(
            title='MetPy Documentation',
            brief_description='Documentation of the MetPy packages',
            description=(f'MetPy includes a set of Python packages useful for metrology applications. '
                         f'Here you can find the documentation of the MetPy packages.'),
            image='documents.png',
            cards=[magnitude]
        )
    ),
    footer=bs.base_footer_template(),
    scripts=bs.base_scripts_template()
)
