"""Functions to build and update documentation."""
from distutils.dir_util import copy_tree

import src.definitions as df


def html_resources(parent=False, grandparent=False):
    """Return the path of the folder that store the HTML resources for MetPy website.

    Parameters
    ----------
    parent : bool, optional
        HTML resource folder in parent folder, default False.
    grandparent : bool, optional
        HTML resource folder in grandparent folder, default False.
    """
    if grandparent:
        path = '../..'
    elif parent:
        path = '..'
    else:
        path = '.'
    return path


def install_from_server(package_name, server_url):
    """Command for package installation from server.

    Parameters
    ----------
    package_name : str
        Package name.
    server_url : str
        URL to custom Python package server.
    """
    return f'pip install {package_name} --extra-index-url {server_url}'


def install_from_github(package_name, author_github_url):
    """Command for package installation from GitHub repository.

    Parameters
    ----------
    package_name : str
        Package name.
    author_github_url : str
        URL to author's GitHub.
    """
    return f'pip install git+{author_github_url}{package_name}.git#egg={package_name}'


def install_from_clone(package_name, author_github_username):
    """Command for package installation from repository clone.

    Parameters
    ----------
    package_name : str
        Package name.
    author_github_username : str
        GitHub username of author.
    """
    command = (f" git clone git@github.com:{author_github_username}/{package_name}.git\n"
               f" cd {package_name}\n"
               f" pip install .")
    return command


def package_link(author_github, name, version):
    """Template of installation link from server.

    Parameters
    ----------
    author_github : str
        URL to author's GitHub.
    name : str
        Package name.
    version : str
        Package version.
    """
    return f'git+{author_github}{name}#egg={name}-{version}" data-requires-python="&gt;=3.6.0'


def build_readme(package, text, update):
    """Build and update the package README.md.

    Parameters
    ----------
    package : str
        Package name.
    text : str
        Package README text.
    update : bool
        True to write the file in the package repository, False to write the file in the metpy repository test folder.
    """
    destination = 'public' if update else 'private'
    file = df.readme_paths[destination][package]
    f = open(file, "w")
    f.write(text)
    f.close()


def build_rst_files(package, rst_texts):
    """Build the package RST files for Sphinx.

    Parameters
    ----------
    package : str
        Package name.
    rst_texts : list
        Texts of package RST documentation files.
    """
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
    """Copy the package RST files for Sphinx to the destination repository.

    Parameters
    ----------
    package : str
        Package name.
    """
    src = df.sphinx_paths[package]['local']['rst']
    dst = df.sphinx_paths[package]['remote']['rst']
    copy_tree(src=src, dst=dst)


def import_html_files(package):
    """Copy the package HTML files of Sphinx from the destination repository.

    Parameters
    ----------
    package : str
        Package name.
    """
    src = df.sphinx_paths[package]['remote']['html']
    dst = df.sphinx_paths[package]['local']['html']
    copy_tree(src=src, dst=dst)


def build_package_docs(package, readme_text, rst_texts, update_readme, export_rst, import_html):
    """Build the documentation of a package.

    Parameters
    ----------
    package : str
        Package name.
    readme_text : str
        Package README text.
    rst_texts : list
        Texts of package RST documentation files.
    update_readme : bool
        True to write the file in the package repository, False to write the file in the metpy repository test folder.
    export_rst : bool
        True to copy the package RST files to the package repository,
        False to write package RST files in the metpy repository test folder.
    import_html : bool
        True to copy the package HTML files from the package repository, False otherwise.
    """
    build_readme(package=package, text=readme_text, update=update_readme)
    build_rst_files(package=package, rst_texts=rst_texts)
    if export_rst:
        export_rst_files(package=package)
    if import_html:
        import_html_files(package=package)


def versions(package):
    """Returns a list of package versions number in ascending order.

    Parameters
    ----------
    package : dict
        Dictionary of named package versions.
    """
    return sorted(list(package.keys()))


def last_version(package):
    """Returns the las version of a package.

    Parameters
    ----------
    package : dict
        Dictionary of named package versions.
    """
    v = sorted(list(package.keys()))
    return v[-1]
