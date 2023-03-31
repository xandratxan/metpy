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
    'index': 'index.html',
    'projects': 'projects.html',
    'server': 'server.html',
    'docs': 'docs.html',
    'magnitude': 'magnitude.html',
}
# HTML files paths
file_paths = {
    'index': './docs/index.html',
    'projects': './docs/projects.html',
    'server': './docs/server.html',
    'docs': './docs/docs.html',
}
# External URLs
external_urls = {
    'ciemat': 'https://www.ciemat.es/portal.do',
    'lmri': 'http://rdgroups.ciemat.es/web/lmri/inicio?p_p_id=2_WAR_kaleodesignerportlet&p_p_lifecycle=0',
}
# HTML cards
projects = {
    'name': 'projects',
    'title': 'MetPy projects',
    'brief_description': 'Projects of the MetPy ecosystem',
    'html_path': html_pages['projects'],
    'image_path': fnc.html_images(parent=False),
    'image_name': 'python.png'
}
server = {
    'name': 'server',
    'title': 'MetPy Python package server',
    'brief_description': 'Python package server for the MetPy packages',
    'html_path': html_pages['server'],
    'image_path': fnc.html_images(parent=False),
    'image_name': 'folder.png'
}
documentation = {
    'name': 'documentation',
    'title': 'MetPy documentation',
    'brief_description': 'Documentation of the MetPy packages',
    'html_path': html_pages['docs'],
    'image_path': fnc.html_images(parent=False),
    'image_name': 'python.png'  # TODO: new icon
}
magnitude = {
    'name': 'magnitude',
    'title': 'physical-magnitude package',
    'brief_description': 'Simple operations with magnitudes including units and uncertainties',
    'html_path': html_pages['magnitude'],
    'image_path': fnc.html_images(parent=False),
    'image_name': 'scale.png'
}
