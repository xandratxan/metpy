"""Functions to build and update documentation."""
import src.definitions as df
from distutils.dir_util import copy_tree


def html_resources(parent=False, grandparent=False):
    """Return the path of the folder that store the HTML resources for MetPy website."""
    if grandparent:
        path = '../..'
    elif parent:
        path = '..'
    else:
        path = '.'
    return path


def install_from_server(package_name, server_url):
    """Command for package installation from server."""
    return f'pip install {package_name} --extra-index-url {server_url}'


def install_from_github(package_name, author_github_url):
    """Command for package installation from GitHub repository."""
    return f'pip install git+{author_github_url}{package_name}.git#egg={package_name}'


def install_from_clone(package_name, author_github_username):
    """Command for package installation from repository clone."""
    command = (f" git clone git@github.com:{author_github_username}/{package_name}.git\n"
               f" cd {package_name}\n"
               f" pip install .")
    return command


def package_link(author_github, name, version):
    """Template of installation link from server."""
    return f'git+{author_github}{name}#egg={name}-{version}" data-requires-python="&gt;=3.6.0'


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


def build_package_docs(package, readme_text, rst_texts, update_readme, export_rst, import_html):
    """Build the documentation of a package."""
    build_readme(package=package, text=readme_text, update=update_readme)
    build_rst_files(package=package, rst_texts=rst_texts)
    if export_rst:
        export_rst_files(package=package)
    if import_html:
        import_html_files(package=package)
