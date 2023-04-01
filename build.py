# Script to build and update documentation
import src.definitions as df
import src.functions as fnc
import src.html.main_pages as main_pages
import src.html.package_pages as package_pages
import src.readme.magnitude as readme_magnitude


def metpy_main_pages():
    files = [
        df.html_paths['main']['index'],
        df.html_paths['main']['packages'],
        df.html_paths['main']['server'],
        df.html_paths['main']['docs'],
    ]
    texts = [
        main_pages.index,
        main_pages.projects,
        main_pages.server,
        main_pages.documentation,
    ]
    fnc.write_files(texts, files)


def metpy_package_pages():
    files = [
        df.html_paths['packages']['magnitude'],
    ]
    texts = [
        package_pages.magnitude,
    ]
    fnc.write_files(texts, files)


def magnitude_package_docs():
    files = [
        df.html_paths['packages']['magnitude'],
        './build/readme_magnitude.md',
    ]
    texts = [
        package_pages.magnitude,
        readme_magnitude.readme_text,
    ]
    fnc.write_files(texts, files)


# Build documentation
if __name__ == '__main__':
    metpy_main_pages()
    magnitude_package_docs()
