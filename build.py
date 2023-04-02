"""Script to build and update documentation."""
import src.definitions as df
import src.functions as fnc
from src.html.pages.documentation import metpy_documentation
from src.html.pages.index import metpy_index
from src.html.pages.packages import metpy_packages, metpy_package_magnitude
from src.html.pages.server import metpy_server, metpy_server_magnitude
from src.readme.magnitude import package_magnitude_readme
# TODO: update readme in destination repo
# TODO: add folder to build and test before update


def get_destination(update):
    return 'public' if update else 'private'


def metpy_pages(update):
    """Build the HTML pages of the MetPy site."""
    destination = get_destination(update=update)
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
    destination = get_destination(update=update)
    files = [
        df.readme_paths[destination]['magnitude'],
        df.html_paths[destination]['packages']['magnitude'],
        df.html_paths[destination]['server']['magnitude'],

    ]
    texts = [
        package_magnitude_readme,
        metpy_package_magnitude,
        metpy_server_magnitude,
    ]
    fnc.write_files(texts, files)


# Build documentation
if __name__ == '__main__':
    metpy_pages(update=False)
    magnitude_package_docs(update=False)
