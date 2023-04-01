# Definitions to build and update documentation
import src.functions as fnc

# Personal information
xcb = {
    'name': 'Xandra Campo',
    'github': 'https://github.com/xandratxan/',
    'github_pages': 'https://xandratxan.github.io/',
    'email': 'xkmpera@gmail.com',
    'github_username': 'xandratxan'
}
# HTML pages paths
html_pages = {
    'main': {
        'index': 'index.html',
        'packages': 'packages.html',
        'server': 'server.html',
        'docs': 'docs.html',
    },
    'packages': {
        'magnitude': 'packages/physical-magnitude.html',
    },

}
# HTML files paths
html_paths = {
    'main': {
        'index': './docs/index.html',
        'packages': './docs/packages.html',
        'server': './docs/server.html',
        'docs': './docs/docs.html',
    },
    'packages': {
        'magnitude': './docs/packages/physical-magnitude.html',
    },

}
# External URLs
external_urls = {
    'ciemat': 'https://www.ciemat.es/portal.do',
    'lmri': 'http://rdgroups.ciemat.es/web/lmri/inicio?p_p_id=2_WAR_kaleodesignerportlet&p_p_lifecycle=0',
}
# HTML cards
main_packages = {
    'name': 'packages',
    'title': 'Packages',
    'brief_description': 'Packages of the MetPy ecosystem',
    'html_path': html_pages['main']['packages'],
    'image_path': fnc.html_images(parent=False),
    'image_name': 'python.png'
}
main_server = {
    'name': 'server',
    'title': 'Python package server',
    'brief_description': 'Python package server for the MetPy packages',
    'html_path': html_pages['main']['server'],
    'image_path': fnc.html_images(parent=False),
    'image_name': 'folder.png'
}
main_documentation = {
    'name': 'documentation',
    'title': 'Documentation',
    'brief_description': 'Documentation of the MetPy packages',
    'html_path': html_pages['main']['docs'],
    'image_path': fnc.html_images(parent=False),
    'image_name': 'python.png'  # TODO: new icon
}
package_magnitude = {  # TODO: refactor
    'name': 'magnitude',
    'title': 'physical-magnitude package',
    'brief_description': 'Simple operations with magnitudes including units and uncertainties',
    'html_path': html_pages['packages']['magnitude'],
    'image_path': fnc.html_images(parent=False),
    'image_name': 'scale.png'
}
docs_magnitude = {  # TODO: refactor, update
    'name': 'magnitude',
    'title': 'physical-magnitude package',
    'brief_description': 'Simple operations with magnitudes including units and uncertainties',
    'html_path': html_pages['packages']['magnitude'],
    'image_path': fnc.html_images(parent=False),
    'image_name': 'scale.png'
}
