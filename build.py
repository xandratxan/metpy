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


def metpy_pages():
    """Build the HTML pages of the MetPy site."""
    files = [
        df.html_paths['main']['index'],
        df.html_paths['main']['packages'],
        df.html_paths['main']['server'],
        df.html_paths['main']['docs'],
        df.html_paths['packages']['magnitude'],
        df.html_paths['server']['magnitude'],
    ]
    texts = [
        metpy_index,
        metpy_packages,
        metpy_server,
        metpy_documentation,
        metpy_package_magnitude,
        metpy_server_magnitude,
    ]
    fnc.write_files(texts, files)


def magnitude_package_docs():
    """Build the documentation of the physical-magnitude package."""
    files = [
        df.readme_paths['origin']['magnitude'],
        df.html_paths['packages']['magnitude'],
        df.html_paths['server']['magnitude'],

    ]
    texts = [
        package_magnitude_readme,
        metpy_package_magnitude,
        metpy_server_magnitude,
    ]
    fnc.write_files(texts, files)


# Build documentation
if __name__ == '__main__':
    metpy_pages()
    # magnitude_package_docs()
