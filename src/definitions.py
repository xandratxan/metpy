"""Definitions to build and update documentation."""
# Personal information of authors and contributors
xcb = {
    'name': 'Xandra Campo',
    'github': 'https://github.com/xandratxan/',
    'github_pages': 'https://xandratxan.github.io/',
    'email': 'xkmpera@gmail.com',
    'github_username': 'xandratxan'
}
rge = {
    'name': 'Ricardo Gomez',
    'github': 'https://github.com/ricargoes/'
}
# HTML pages paths of MetPy website
html_pages = {
    'index': 'index.html',
    'packages': {
        'index': 'packages.html',
        'magnitude': 'packages/magnitude.html',
    },
    'server': {
        'index': 'server/index.html',
        'magnitude': 'physical-magnitude/index.html',
    },
    'documentation': {
        'index': 'docs.html',
        'magnitude': 'docs/physical-magnitude/index.html',
    },

}
# HTML file paths for documentation building
html_paths = {
    'public': {
        'index': './docs/index.html',
        'packages': {
            'index': './docs/packages.html',
            'magnitude': './docs/packages/magnitude.html',
        },
        'server': {
            'index': './docs/server/index.html',
            'magnitude': './docs/server/physical-magnitude/index.html',
        },
        'documentation': './docs/docs.html',
    },
    'private': {
        'index': './build/docs/index.html',
        'packages': {
            'index': './build/docs/packages.html',
            'magnitude': './build/docs/packages/magnitude.html',
        },
        'server': {
            'index': './build/docs/server/index.html',
            'magnitude': './build/docs/server/physical-magnitude/index.html',
        },
        'documentation': './build/docs/docs.html',
    },

}
# README file paths for documentation building
readme_paths = {
    'private': {
        'magnitude': './build/readme/magnitude.md'
    },
    'public': {
        'magnitude': '/home/txan/PycharmProjects/physical-magnitude/README.md'
    },
}
# External URLs
external_urls = {
    'ciemat': 'https://www.ciemat.es/portal.do',
    'lmri': 'http://rdgroups.ciemat.es/web/lmri/inicio?p_p_id=2_WAR_kaleodesignerportlet&p_p_lifecycle=0',
    'design': 'https://html5up.net',
    'icons': 'https://www.flaticon.com/',
}
# Packages information
server = {
    'name': 'python-package-server',
    'brief_description': 'PyPi-like package server for the MetPy packages',
    'description': (
        f'This website server as a PyPi-like package server for the MetPy packages. '
        f'It conforms to Pep 503. It is based on a blog post by freeCodeCamp.'),  # TODO: how to add links HTML, README
    'image': 'folder.png',
    'url_server': f"https://xandratxan.github.io/python-package-server/",  # TODO: update
}
magnitude = {
    'name': 'physical-magnitude',
    'brief_description': 'Simple operations with magnitudes including units and uncertainties',
    'url_source_code': f"{xcb['github']}physical-magnitude/",
    'url_issues': f"{xcb['github']}physical-magnitude/issues/",
    'url_documentation': f"{xcb['github_pages']}physical-magnitude/",
    'last_version': '0.1.0',
    'last_release': 'March 2023',
    'license': 'GNU GPL 3.0',
    'description': (
        f'This package allows to perform simple operations with magnitudes including units and uncertainties. '
        f'It allows to define magnitudes with value, uncertainty and unit. '
        f'It allows to compute simple operations providing the result not only for the magnitude value, '
        f'but also its uncertainty and unit.'
        f'Available operations include summation, subtraction, multiplication and division.'),
    'image': 'scale.png',
    'import': 'from magnitude import Magnitude',
    'versions': ['0.1.0']
}
# Miscellanea
non_stable_msg = 'This package is under active development. The current version is considered non-stable.'
