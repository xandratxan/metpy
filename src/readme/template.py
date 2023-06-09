"""Template for package README file."""
import src.definitions as df


def readme(name, brief_description, description,
           last_version, license_info, url_source_code, url_issues, url_documentation,
           non_stable_msg, install_from_server, install_from_github, install_from_clone,
           code_snippet, snippet_output, release_history, authors):
    """Markdown template for package README file.

    Parameters
    ----------
    name : str
        Package name.
    brief_description : str
        Package brief description.
    description : str
        Package description.
    last_version : str
        Package last version number.
    license_info : str
        Package license information.
    url_source_code : str
        URL to package repository source code on GitHub.
    url_issues : str
        URL to package repository issues on GitHub.
    url_documentation : str
        URL to package documentation on GitHub Pages.
    non_stable_msg : str
        Non-stable version warning message.
    install_from_server : str
        Command to install package via pip from custom server.
    install_from_github : str
        Command to install package via pip from GitHub repository.
    install_from_clone : str
        Command to install package via pip cloning the GitHub repository.
    code_snippet : str
        Package code snippet input.
    snippet_output : str
        Package code snippet output.
    release_history : str
        Package release history.
    authors : str
        Package authors and contributors.
    """
    text = (
        f"# Package {name}\n"
        f"\n"
        f"> {brief_description}.\n"
        f"\n"
        f"| Last version: {last_version} | License: {license_info} | "
        f"[Source code]({url_source_code}) | [Issues]({url_issues}) | [Documentation]({url_documentation}) |\n"
        f"|--------------------|--------------------|--------------------|--------------------|--------------------|\n"
        f"\n"
        f"> **WARNING**: {non_stable_msg}.\n"
        f"\n"
        f"Package ``{name}`` {description}\n"
        f"\n"
        f"## Installation\n"
        f"\n"
        f"``{name}`` can be installed in three different ways.\n"
        f"\n"
        f"Install via pip from PyPi-like server:\n"
        f"\n"
        f"```bash\n"
        f"{install_from_server}\n"
        f"```\n"
        f"\n"
        f"Install via pip with GitHub repository url:\n"
        f"\n"
        f"```bash\n"
        f"{install_from_github}\n"
        f"```\n"
        f"\n"
        f"Clone GitHub repository and install via pip:\n"
        f"\n"
        f"```bash\n"
        f"{install_from_clone}\n"
        f"```\n"
        f"\n"
        f"## Usage\n"
        f"\n"
        f"{code_snippet}\n"
        f"\n"
        f"Output:\n"
        f"\n"
        f"{snippet_output}\n"
        f"\n"
        f"## Release History\n"
        f"\n"
        f"{release_history}\n"
        f"\n"
        f"## Authors and contributors\n"
        f"\n"
        f"{authors}\n"
    )
    return text


def releases(versions):
    """Markdown template for package Release history section of README file.

    Parameters
    ----------
    versions : dict
        Package versions dictionary.
    """
    text = ''
    for key, value in versions.items():
        text += (f"* {key}\n"
                 f"    * {value}\n")
    return text


def author_contributor(contributor=False):
    """Markdown template for package Authors and contribution section of README file.

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
        f": {author_name},\n"
        f"[@GitHub]({author_github})\n"
    )
    if contributor:
        text += (
            f"\n"
            f"Contributors:\n"
            f": {contributor_name},\n"
            f"[@GitHub]({contributor_github})"
        )
    return text
