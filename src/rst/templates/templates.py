"""RST templates for package documentation."""
import src.definitions as df


def index_template(name, description, non_stable_msg, versions, contributors,
                   last_version, url_source_code, url_issues, license_info):
    """RST template for package documentation index.

    Parameters
    ----------
    name : str
        Package name.
    description : str
        Package description.
    non_stable_msg : str
        Non-stable version warning message.
    versions : dict
        Package versions dictionary.
    contributors : bool, optional
        True if package has a single author and a single contributor, False if package has a single author.
    last_version : str
        Package last version number.
    url_source_code : str
        URL to package repository source code on GitHub.
    url_issues : str
        URL to package repository issues on GitHub.
    license_info : str
        Package license information.
    """
    authors = author_contributor(contributor=contributors)
    history = release_history(versions)
    text = (
        f"Welcome to ``{name}``'s documentation!\n"
        f"==================================================\n"
        f"\n"
        f".. admonition:: Information\n"
        f"\n"
        f"   Last version: {last_version} | License: {license_info} | "
        f"   `Source code <{url_source_code}>`_ | `Issues <{url_issues}>`_\n"
        f"\n"
        f"Package ``{name}`` {description}\n"
        f"\n"
        f".. warning::\n"
        f"   {non_stable_msg}\n"
        f"\n"
        f".. toctree::\n"
        f"   tutorial\n"
        f"   howto\n"
        f"   api\n"
        f"   :maxdepth: 4\n"
        f"   :caption: Contents\n"
        f"\n"
        f"Indices and tables\n"
        f"------------------\n"
        f"\n"
        f"* :ref:`genindex`\n"
        # f"* :ref:`modindex`\n"
        # f"* :ref:`search`\n"
        f"\n"
        f"Release History\n"
        f"---------------\n"
        f"\n"
        f"{history}"
        f"\n"
        f"Authors and contributors\n"
        f"------------------------\n"
        f"\n"
        f"{authors}"
    )
    return text


def release_history(versions):
    """RST template for package release history section of package documentation index.

    Parameters
    ----------
    versions : dict
        Package versions dictionary."""
    text = ''
    for key, value in versions.items():
        text += (f"* {key}\n"
                 f"    * {value}\n")
    return text


def author_contributor(contributor=False):
    """RST template for package authors and contributors section of package documentation index.

    Parameters
    ----------
    contributor : bool, optional
        True if package has a single author and a single contributor, False if package has a single author.
    """
    author_name = df.xcb['name']
    author_github = df.xcb['github']
    contributor_name = df.rge['name']
    contributor_github = df.rge['github']
    text = (
        f"Author:\n"
        f"    {author_name},\n"
        f"    `@GitHub <{author_github}>`_,\n"
    )
    if contributor:
        text += (
            f"\n"
            f"Contributors:\n"
            f"    {contributor_name},\n"
            f"    `@GitHub <{contributor_github}>`_\n"
        )
    return text


def tutorial_template(name, install_from_server, install_from_github, install_from_clone, tutorial):
    """RST template for package documentation tutorial.

    Parameters
    ----------
    name : str
        Package name.
    install_from_server : str
        Command to install package via pip from custom server.
    install_from_github : str
        Command to install package via pip from GitHub repository.
    install_from_clone : str
        Command to install package via pip cloning the GitHub repository.
    tutorial : str
        Package tutorial section.
    """
    text = (
        f"Tutorial\n"
        f"========\n"
        f"\n"
        f"This tutorial is a good introduction on how to get started with ``{name}``.\n"
        f"\n"
        f".. contents:: Table of Contents\n"
        f"\n"
        f"Installation\n"
        f"------------\n"
        f"\n"
        f"``{name}`` can be installed in three different ways.\n"
        f"\n"
        f"Install via pip from PyPi-like server:\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    {install_from_server}\n"
        f"\n"
        f"Install via pip with GitHub repository url:\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"    {install_from_github}\n"
        f"\n"
        f"Clone GitHub repository and install via pip:\n"
        f"\n"
        f".. code-block::\n"
        f"\n"
        f"{install_from_clone}\n"
        f"\n"
        f"{tutorial}"
    )
    return text


def howto_template(name, howto):
    """RST template for package documentation how-to.

    Parameters
    ----------
    name : str
        Package name.
    howto : str
        Package how-to section.
    """
    text = (
        f"How to guides\n"
        f"=============\n"
        f"\n"
        f"This part of the documentation describes how to accomplish common tasks with ``{name}``.\n"
        f"\n"
        f".. contents:: Table of Contents\n"
        f"\n"
        f"{howto}"
    )
    return text


def api_template(name, api):
    """RST template for package documentation API.

    Parameters
    ----------
    name : str
        Package name.
    api : str
        Package API section.
    """
    text = (
        f"API Reference\n"
        f"=============\n"
        f"\n"
        f"This part of the documentation covers all the public interfaces of ``{name}``.\n"
        f"\n"
        f"{api}"
    )
    return text
