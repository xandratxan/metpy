"""Package/Server section HTML templates for MetPy website."""
import src.definitions as df
import src.functions as fnc


def package_template(title, information, warning, description, installation, code_snippet):
    """Package section HTML templates for MetPy website.

    Parameters
    ----------
    title : str
        Section title.
    information : str
        Package information.
    warning : str
        Non-stable warning.
    description : str
        Package description.
    installation : str
        Package installation instructions.
    code_snippet : str
        Package code snippet.
    """
    i = 12
    text = (
        f'{" " * i}<!-- Package -->\n'
        f'{" " * i}<section class="post">\n'
        f'{title}'
        f'{information}'
        f'{warning}'
        f'{description}'
        f'{installation}'
        f'{code_snippet}'
        f'{" " * i}</section>\n'
    )
    return text


def server_template(title, warning, description, installation, packages_table):
    """Server section HTML templates for MetPy website.

    Parameters
    ----------
    title : str
        Section title.
    warning : str
        Non-stable warning.
    description : str
        Package description.
    installation : str
        Package installation instructions.
    packages_table : str
        Packages table.
    """
    i = 12
    text = (
        f'{" " * i}<!-- Package -->\n'
        f'{" " * i}<section class="post">\n'
        f'{title}'
        f'{warning}'
        f'{description}'
        f'{installation}'
        f'{packages_table}'
        f'{" " * i}</section>\n'
    )
    return text


def title_template(title, brief_description, image, parent=False, grandparent=False):
    """Title section HTML template of package/server section for MetPy website.

    Parameters
    ----------
    title : str
        Package title.
    brief_description : str
        Package brief description.
    image : str
        Package image file name.
    parent : bool, optional
        HTML resource folder in parent folder, default False.
    grandparent : bool, optional
        HTML resource folder in grandparent folder, default False.
    """
    i = 12
    path = fnc.html_resources(parent=parent, grandparent=grandparent)
    text = (
        f'{" " * i}<!-- Title and subtitle -->\n'
        f'{" " * i}<header class="major">\n'
        f'{" " * i}    <h1>{title}</h1>\n'
        f'{" " * i}    <p>{brief_description}</p>\n'
        f'{" " * i}    <div class="row">\n'
        f'{" " * i}        <div class="col-5 col-12-small"></div>\n'
        f'{" " * i}        <div class="col-2 col-12-small">\n'
        f'{" " * i}            <span class="image fit"><img src="{path}/images/{image}" alt="{image}" /></span>\n'
        f'{" " * i}        </div>\n'
        f'{" " * i}        <div class="col-5 col-12-small"></div>\n'
        f'{" " * i}    </div>\n'
        f'{" " * i}</header>\n'
    )
    return text


def info_template(last_version, license_info, url_source_code, url_issues, url_documentation):
    """Package information section HTML template of package section for MetPy website.

    Parameters
    ----------
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
    """
    i = 12
    text = (
        f'{" " * i}<!-- Useful information -->\n'
        f'{" " * i}<div class="table-wrapper">\n'
        f'{" " * i}    <table>\n'
        f'{" " * i}        <tbody>\n'
        f'{" " * i}            <tr>\n'
        f'{" " * i}                <td>Last version</b>: {last_version}</td>\n'
        f'{" " * i}                <td>License</b>: {license_info}</td>\n'
        f'{" " * i}                <td><a href="{url_source_code}">Source code</a></td>\n'
        f'{" " * i}                <td><a href="{url_documentation}">Documentation</a></td>\n'
        f'{" " * i}                <td><a href="{url_issues}">Issues</a><br/></td>\n'
        f'{" " * i}            </tr>\n'
        f'{" " * i}        </tbody>\n'
        f'{" " * i}    </table>\n'
        f'{" " * i}</div>\n'
    )
    return text


def warning_template(message):
    """Warning section HTML template of package/server section for MetPy website.

    Parameters
    ----------
    message : str
        Warning message.
    """
    i = 12
    text = (
        f'{" " * i}<!-- Warning -->\n'
        f'{" " * i}<div class="box">\n'
        f'{" " * i}    <p><b>WARNING</b>: {message}</p>\n'
        f'{" " * i}</div>\n'
    )
    return text


def description_template(name, description):
    """Package description section HTML template of package/server section for MetPy website.

    Parameters
    ----------
    name : str
        Package name.
    description : str
        Package description.
    """
    i = 12
    text = (
        f'{" " * i}<!-- Description -->\n'
        f'{" " * i}<p>Package <code>{name}</code> {description}</p>\n'
    )
    return text


def server_description_template():
    """Server description section HTML template of package/server section for MetPy website."""
    pep503 = df.external_urls['pep503']
    blog_post = df.external_urls['blog post']
    i = 12
    text = (
        f'{" " * i}<!-- Description -->\n'
        f'{" " * i}<p>\n'
        f'{" " * i}This website serves as a PyPI-like Python package server for the MetPy packages. '
        f'{" " * i}It conforms to <a href="{pep503}" title="python icons">Pep 503</a>. '
        f'{" " * i}It is based on a <a href="{blog_post}" title="python icons">blog post</a> by freeCodeCamp.\n'
        f'{" " * i}</p>\n'
    )
    return text


def installation_template(is_server, install_from_server):
    """Installation section HTML template of package/server section for MetPy website.

    Parameters
    ----------
    is_server : bool
        True if the installation instructions are for the server section, False otherwise.
    install_from_server : str
        Command to install a package via pip from custom server.
    """
    i = 12
    if is_server:
        text = (
            f'{" " * i}<!-- Installation -->\n'
            f'{" " * i}<p>The packages available in this server can be used to specify dependencies in\n'
            f'{" " * i}   <code>pyproject.toml</code> files including the entry\n'
            f'{" " * i}   <code>dependencies = ["package-name"]</code>\n'
            f'{" " * i}   They can also be installed via <code>pip</code>:<br/>\n'
            f'{" " * i}   <code>{install_from_server}</code></p>\n'
        )
    else:
        text = (
            f'{" " * i}<!-- Installation -->\n'
            f'{" " * i}<p>This package can be installed via <code>pip</code>:<br/>\n'
            f'{" " * i}   <code>{install_from_server}</code></p>\n'
        )
    return text


def code_snippet_template(name, code, output):
    """Code snippet section HTML template of package section for MetPy website.

    Parameters
    ----------
    name : str
        Package name.
    code : str
        Package code snippet input.
    output : str
        Package code snippet output.
    """
    i = 12
    text = (
        f'{" " * i}<!-- Code snippet -->\n'
        f'{" " * i}<p>Below you can find a code snippet to illustrate how to work with '
        f'{" " * i}   <code>{name}</code> package:</p>\n'
        f'{" " * i}<pre><code class="language-python line-numbers" data-prismjs-copy="Copy">'
        f'{code}\n'
        f'{" " * i}</code></pre>\n'
        f'{" " * i}<p>Below you can find the snippet output:</p>\n'
        f'{" " * i}<pre><code class="language-python line-numbers" data-prismjs-copy="Copy">'
        f'{output}\n'
        f'{" " * i}</code></pre>\n'
    )
    return text


def packages_table_template(columns, packages, versions=False, parent=False, grandparent=False):
    """Package table HTML template of server section for MetPy website.

    Parameters
    ----------
    columns : list
        List of table column headers.
    packages : list or dict
        Dictionaries of package information for packages table or package dictionary for package versions table.
    versions : bool, optional
        True if the table is to list package versions, False if table is to list packages, default False.
    parent : bool, optional
        HTML resource folder in parent folder, default False.
    grandparent : bool, optional
        HTML resource folder in grandparent folder, default False.
    """
    i = 12
    path = fnc.html_resources(parent=parent, grandparent=grandparent)
    body = ''
    if versions:
        for version in packages['versions']:
            body += packages_table_row_template(
                path=path,
                image='folder.png',
                html_path=fnc.package_link(author_github=df.xcb['github'], name=packages['name'], version=version),
                name=f"{packages['name']}-{version}",
                description=version
            )
    else:
        for package in packages:
            body += packages_table_row_template(
                path=path,
                image=package['image'],
                html_path=package['html_path'],
                name=package['name'],
                description=package['brief_description']
            )
    table = (
        f'{" " * i}<!-- Packages -->\n'
        f'{" " * i}<p>The following packages are available:</p>\n'
        f'{" " * i}<div class="table-wrapper">\n'
        f'{" " * i}    <table>\n'
        f'{" " * i}        <thead>\n'
        f'{" " * i}            <tr>\n'
        f'{" " * i}                <th></th>\n'
        f'{" " * i}                <th>{columns[0]}</th>\n'
        f'{" " * i}                <th>{columns[1]}</th>\n'
        f'{" " * i}            </tr>\n'
        f'{" " * i}        </thead>\n'
        f'{" " * i}        <tbody>\n'
        f'{body}'
        f'{" " * i}        </tbody>\n'
        f'{" " * i}    </table>\n'
        f'{" " * i}</div>\n'
    )
    return table


def packages_table_row_template(path, image, html_path, name, description):
    """Package table row HTML template of server section for MetPy website.

    Parameters
    ----------
    path : str
        Path to HTML resources folder.
    image : str
        Package image.
    html_path : str
        Link to package details.
    name : str
        Package name.
    description : str
        Package description.
    """
    i = 24
    row = (
        f'{" " * i}<tr>\n'
        f'{" " * i}    <td style="text-align: center; vertical-align: middle;">\n'
        f'{" " * i}        <img src="{path}/images/{image}" alt="{image}" width="40" height="40">\n'
        f'{" " * i}    </td>\n'
        f'{" " * i}    <td><a href="{html_path}">{name}</a></td>\n'
        f'{" " * i}    <td>{description}</td>\n'
        f'{" " * i}</tr>\n'
    )
    return row
