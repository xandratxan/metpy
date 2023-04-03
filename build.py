"""Script to build and update documentation."""

import src.definitions as df
import src.functions as fnc
import src.html.pages.documentation as metpy_documentation
import src.html.pages.index as metpy_index
import src.html.pages.packages as metpy_packages
import src.html.pages.server as metpy_server
import src.readme.magnitude as magnitude_readme
import src.rst.magnitude as magnitude_rst


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
        metpy_index.index,
        metpy_packages.packages,
        metpy_packages.package_magnitude,
        metpy_server.server,
        metpy_server.server_magnitude,
        metpy_documentation.documentation,
    ]
    for text, file in zip(texts, files):
        f = open(file, "w")
        f.write(text)
        f.close()


def build_magnitude_docs(update_readme, export_rst, import_html):
    """Build the documentation of the physical-magnitude package."""
    package = 'magnitude'
    readme_text = magnitude_readme.readme
    rst_texts = [
        magnitude_rst.index,
        magnitude_rst.tutorial,
        magnitude_rst.howto,
        magnitude_rst.api,
    ]
    fnc.build_package_docs(package=package, readme_text=readme_text, rst_texts=rst_texts,
                           update_readme=update_readme, export_rst=export_rst, import_html=import_html)


if __name__ == '__main__':
    update_local = False
    update_package = False
    update_public = False
    if update_local:
        # MODIFY LOCAL REPOSITORY
        # Build MetPy page in local test folder
        metpy_pages(update=False)
        # Build package documentation in local test folder
        build_magnitude_docs(update_readme=False, export_rst=False, import_html=False)
    if update_package:
        # MODIFY PACKAGE REPOSITORY
        # Build package documentation and export to package repository (use Sphinx to generate HTML documentation)
        build_magnitude_docs(update_readme=True, export_rst=True, import_html=True)
    if update_public:
        # MODIFY PUBLIC REPOSITORY
        # Build MetPy page in local public folder (push to publish)
        metpy_pages(update=True)
        # Import package documentation from package repository (push to publish)
        build_magnitude_docs(update_readme=False, export_rst=False, import_html=True)
