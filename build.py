"""Script to build and update documentation."""
import src.definitions as df
import src.functions as fnc
from src.html.pages.documentation import metpy_documentation
from src.html.pages.index import metpy_index
from src.html.pages.packages import metpy_packages, metpy_package_magnitude
from src.html.pages.server import metpy_server, metpy_server_magnitude
from src.readme.magnitude import package_magnitude_readme
from src.rst.magnitude.index import package_magnitude_index


def metpy_pages(update):
    """Build the HTML pages of the MetPy site."""
    destination = fnc.get_destination(update=update)
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
    fnc.write_files(texts, files)


def magnitude_package_docs(update):
    """Build the documentation of the physical-magnitude package."""
    destination = fnc.get_destination(update=update)
    files = [
        df.readme_paths[destination]['magnitude'],
        df.rst_paths['magnitude']['index'],
        df.html_paths[destination]['packages']['magnitude'],
        df.html_paths[destination]['server']['magnitude'],

    ]
    texts = [
        package_magnitude_readme,
        package_magnitude_index,
        metpy_package_magnitude,
        metpy_server_magnitude,
    ]
    fnc.write_files(texts, files)


if __name__ == '__main__':
    # Build documentation
    update_docs = False
    metpy_pages(update=update_docs)
    magnitude_package_docs(update=update_docs)
