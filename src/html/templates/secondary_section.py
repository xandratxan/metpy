"""Secondary section HTML templates for MetPy website."""
import src.definitions as df
import src.functions as fnc


def package_template(title, information, warning, description, installation, code_snippet):
    """Package section HTML templates for MetPy website."""
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
    """Server section HTML templates for MetPy website."""
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
    """Template of title section of secondary section HTML templates for MetPy website."""
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


def info_template(last_version, last_release, license_info, url_source_code, url_issues, url_documentation):
    """Template of information section of secondary section HTML templates for MetPy website."""
    i = 12
    text = (
        f'{" " * i}<!-- Useful information -->\n'
        f'{" " * i}<div class="box">\n'
        f'{" " * i}    <div class="row">\n'
        f'{" " * i}        <div class="col-4 col-12-small">\n'
        f'{" " * i}            <b>Last version</b>: {last_version}<br/>\n'
        f'{" " * i}            <b>Last release</b>: {last_release}\n'
        f'{" " * i}        </div>\n'
        f'{" " * i}        <div class="col-4 col-12-small">\n'
        f'{" " * i}            <b>Source code</b>: <a href="{url_source_code}">GitHub</a><br/>\n'
        f'{" " * i}            <b>Documentation</b>: <a href="{url_documentation}">GitHub</a>\n'
        f'{" " * i}        </div>\n'
        f'{" " * i}        <div class="col-3 col-12-small">\n'
        f'{" " * i}            <b>Issues</b>: <a href="{url_issues}">GitHub</a><br/>\n'
        f'{" " * i}            <b>License</b>: {license_info}\n'
        f'{" " * i}        </div>\n'
        f'{" " * i}    </div>\n'
        f'{" " * i}</div>\n'
    )
    return text


def warning_template(message):
    """Template of warning section of secondary section HTML templates for MetPy website."""
    i = 12
    text = (
        f'{" " * i}<!-- Warning -->\n'
        f'{" " * i}<div class="box">\n'
        f'{" " * i}    <p><b>WARNING</b>: {message}</p>\n'
        f'{" " * i}</div>\n'
    )
    return text


def description_template(description):
    """Template of description section of secondary section HTML templates for MetPy website."""
    i = 12
    text = (
        f'{" " * i}<!-- Description -->\n'
        f'{" " * i}<p>{description}</p>\n'
    )
    return text


def installation_template(is_server, install_from_server):
    """Template of installation section of secondary section HTML templates for MetPy website."""
    i = 12
    # Template for section of package pages at my website at GitHub Pages
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
    """Template of code snippet section of secondary section HTML templates for MetPy website."""
    i = 12
    # Template for section of package pages at my website at GitHub Pages
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
    """Template of table of packages of secondary section HTML templates for MetPy website."""
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
    """Template of table of packages row of secondary section HTML templates for MetPy website."""
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
