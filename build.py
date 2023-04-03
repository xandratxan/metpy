"""Script to build and update documentation."""

import src.definitions as df
import src.functions as fnc
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


def build_magnitude_docs(update_readme, export_rst, import_html):
    """Build the documentation of the physical-magnitude package."""
    package = 'magnitude'
    readme_text = package_magnitude_readme
    rst_texts = [
        package_magnitude_index,
        package_magnitude_tutorial,
        package_magnitude_howto,
        package_magnitude_api,
    ]
    fnc.build_package_docs(package=package, readme_text=readme_text, rst_texts=rst_texts,
                           update_readme=update_readme, export_rst=export_rst, import_html=import_html)


if __name__ == '__main__':
    # Build documentation
    metpy_pages(update=False)
    build_magnitude_docs(update_readme=False, export_rst=False, import_html=True)
