"""RST templates for package documentation index."""
import src.definitions as df


def index_template(name, description, non_stable_msg, versions, contributors,
                   last_version, last_release, url_source_code, url_documentation, url_issues, license_info):
    """RST template for package documentation index."""
    authors = author_contributor(contributor=contributors)
    history = release_history(versions)
    text = (
        f"Welcome to ``{name}``'s documentation!\n"
        f"==================================================\n"
        f"\n"
        f"{description}\n"
        f"\n"
        f".. note::\n"
        f"   {non_stable_msg}\n"
        f"\n"
        f":Last version: {last_version}\n"
        f":Last release: {last_release}\n"
        f":Source code: `GitHub <{url_source_code}>`_\n"
        f":Documentation: `GitHub Pages <{url_documentation}>`_\n"
        f":Issues: `GitHub <{url_issues}>`_\n"
        f":License: {license_info}\n"
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
        f"* :ref:`modindex`\n"
        f"* :ref:`search`\n"
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
    """RST template for release history section of package documentation index."""
    text = ''
    for key, value in versions.items():
        text += (f"* {key}\n"
                 f"    * {value}\n")
    return text


def author_contributor(contributor=False):
    """RST template for authors and contributors section of package documentation index."""
    author_name = df.xcb['name']
    author_email = df.xcb['email']
    author_github = df.xcb['github']
    author_github_pages = df.xcb['github_pages']
    contributor_name = df.rge['name']
    contributor_github = df.rge['github']
    text = (
        f"Author:\n"
        f"    {author_name},\n"
        f"    `@GitHub <{author_github}>`_,\n"
        f"    `@GitHub Pages <{author_github_pages}>`_,\n"
        f"    {author_email}\n"
    )
    if contributor:
        text += (
            f"\n"
            f"Contributors:\n"
            f"    {contributor_name},\n"
            f"    `@GitHub <{contributor_github}>`_\n"
        )
    return text
