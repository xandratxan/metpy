"""HTML index pages of MetPy website."""
import src.definitions as df
import src.html.templates.base as bs
import src.html.templates.main_section as ms

# Project cards
packages = {
    'name': 'packages',
    'title': 'Packages',
    'brief_description': 'Packages of the MetPy ecosystem',
    'html_path': df.html_pages['packages']['index'],
    'image': 'python.png'
}
server = {
    'name': 'server',
    'title': 'Package server',
    'brief_description': 'Python package server for the MetPy packages',
    'html_path': df.html_pages['server']['index'],
    'image': 'folder.png'
}
documentation = {
    'name': 'documentation',
    'title': 'Documentation',
    'brief_description': 'Documentation of the MetPy packages',
    'html_path': df.html_pages['documentation']['index'],
    'image': 'documents.png'
}
# MetPy website index page
index = bs.base_template(
    title='MetPy',
    header=bs.base_header_template(active='index'),
    main=bs.base_main_template(
        main=ms.main_section_template(
            title='Metrology & Python',
            brief_description=f'An ecosystem of Python projects for metrology',
            description=(f'MetPy is an ecosystem of Python projects for metrology. '
                         f'It includes a set of Python packages and a '
                         f'PyPI-like package server to provide those packages. '
                         f'Here you can find the packages of the MetPy ecosystem, '
                         f'the server of the MetPy packages and the documentation of the MetPy packages.'),
            image='',
            cards=[packages, server, documentation]
        )
    ),
    footer=bs.base_footer_template(),
    scripts=bs.base_scripts_template()
)
