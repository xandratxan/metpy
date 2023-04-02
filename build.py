"""Script to build and update documentation."""
from distutils.dir_util import copy_tree

import src.definitions as df
from src.html.pages.documentation import metpy_documentation
from src.html.pages.index import metpy_index
from src.html.pages.packages import metpy_packages, metpy_package_magnitude
from src.html.pages.server import metpy_server, metpy_server_magnitude
from src.readme.magnitude import package_magnitude_readme
from src.rst.magnitude import package_magnitude_index, package_magnitude_tutorial, package_magnitude_api, \
    package_magnitude_howto


def metpy_pages(update):
    """Build the HTML pages of the MetPy site."""
    destination = 'public' if update else 'private'
    files = [
        df.html_paths[destination]['index'],
        df.html_paths[destination]['packages']['index'],
        df.html_paths[destination]['packages']['magnitude'],
        df.html_paths[destination]['server']['index'],
        df.html_paths[destination]['server']['magnitude'],
        df.html_paths[destination]['documentation'],
    ]
    texts = [
        metpy_index,
        metpy_packages,
        metpy_package_magnitude,
        metpy_server,
        metpy_server_magnitude,
        metpy_documentation,
    ]
    for text, file in zip(texts, files):
        f = open(file, "w")
        f.write(text)
        f.close()


def build_readme(package, text, update):
    """Build and update the package README.md."""
    destination = 'public' if update else 'private'
    file = df.readme_paths[destination][package]
    f = open(file, "w")
    f.write(text)
    f.close()


def build_rst_files(package, rst_texts):
    """Build the package RST files for Sphinx."""
    rst_files = [
        df.rst_paths[package]['index'],
        df.rst_paths[package]['tutorial'],
        df.rst_paths[package]['howto'],
        df.rst_paths[package]['api'],
    ]
    for text, file in zip(rst_texts, rst_files):
        f = open(file, "w")
        f.write(text)
        f.close()


def export_rst_files(package):
    """Copy the package RST files for Sphinx to the destination repository."""
    src = df.sphinx_paths[package]['local']['rst']
    dst = df.sphinx_paths[package]['remote']['rst']
    copy_tree(src=src, dst=dst)


def import_html_files(package):
    """Copy the package HTML files of Sphinx from the destination repository."""
    src = df.sphinx_paths[package]['remote']['html']
    dst = df.sphinx_paths[package]['local']['html']
    copy_tree(src=src, dst=dst)


def build_package_docs(package, rst_texts, update_readme, export_rst, import_html):
    """Build the documentation of the physical-magnitude package."""
    build_readme(package=package, text=package_magnitude_readme, update=update_readme)
    build_rst_files(package=package, rst_texts=rst_texts)
    if export_rst:
        export_rst_files(package=package)
    if import_html:
        import_html_files(package=package)


def build_magnitude_docs(update_readme, export_rst, import_html):
    package = 'magnitude'
    rst_texts = [
        package_magnitude_index,
        package_magnitude_tutorial,
        package_magnitude_howto,
        package_magnitude_api,
    ]
    build_package_docs(package, rst_texts, update_readme, export_rst, import_html)


if __name__ == '__main__':
    # Build documentation
    metpy_pages(update=False)
    build_magnitude_docs(update_readme=False, export_rst=False, import_html=True)
