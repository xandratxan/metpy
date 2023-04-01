# HTML templates for secondary sections at MetPy website

def package_template(title, information, warning, description, installation, code_snippet):
    # Template for package page at MetPy website
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


def title_template(parent, title, brief_description, image):
    # Template for section pages at my website at GitHub Pages (package server page and package pages)
    i = 12
    if parent:
        path = '..'
    else:
        path = '.'
    text = (
        f'{" " * i}<!-- Title and subtitle -->\n'
        f'{" " * i}<header class="major">\n'
        f'{" " * i}    <h1>{title}</h1>\n'
        f'{" " * i}    <p>{brief_description}</p>\n'
        f'{" " * i}    <img src="{path}/images/{image}" alt="" width="100" height="100">\n'
        f'{" " * i}</header>\n'
    )
    return text


def info_template(last_version, last_release, license_info, url_source_code, url_issues, url_documentation):
    # Template for section pages at my website at GitHub Pages (package server page and package pages)
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
    # Template for section pages at my website at GitHub Pages (package server page and package pages)
    i = 12
    text = (
        f'{" " * i}<!-- Warning -->\n'
        f'{" " * i}<div class="box">\n'
        f'{" " * i}    <p><b>WARNING</b>: {message}</p>\n'
        f'{" " * i}</div>\n'
    )
    return text


def description_template(description):
    i = 12
    text = (
        f'{" " * i}<!-- Description -->\n'
        f'{" " * i}<p>\n'
        f'{" " * i}{description}\n'
        f'{" " * i}</p>\n'
    )
    return text


def installation_template(is_server, install_from_server):
    i = 12
    # Template for section of package pages at my website at GitHub Pages
    if is_server:
        text = (
            f'{" " * i}<!-- Installation -->\n'
            f'{" " * i}<p>The packages available in this server can be used to specify dependencies in\n'
            f'{" " * i}   <code>pyproject.toml</code> files including the entry <code>dependencies = ["package-name"]</code>\n'
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
    i = 12
    # Template for section of package pages at my website at GitHub Pages
    text = (
        f'{" " * i}<!-- Code snippet -->\n'
        f'{" " * i}<p>Below you can find a code snippet to illustrate how to work with <code>{name}</code> package:</p>\n'
        f'{" " * i}<pre><code class="language-python line-numbers" data-prismjs-copy="Copy">'
        f'{code}\n'
        f'{" " * i}</code></pre>\n'
        f'{" " * i}<p>Below you can find the snippet output:</p>\n'
        f'{" " * i}<pre><code class="language-python line-numbers" data-prismjs-copy="Copy">'
        f'{output}\n'
        f'{" " * i}</code></pre>\n'
    )
    return text


def packages_table_template(package_server_link, columns, packages):
    # Template for packages table in the section of package server page at my website at GitHub Pages
    i = 12
    head = (
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
    )
    body = ''
    for name, description, html_path, image_path in packages:
        body += f'<tr>\n'
        body += f'    <td><img src="{image_path}" alt="" width="30" height="30"></td>\n'
        if package_server_link:
            body += f'    <td><a {html_path}>{name}</a></td>\n'
        else:
            body += f'    <td><a href="{html_path}">{name}</a></td>\n'
        body += f'    <td>{description}</td>\n'
        body += f'</tr>\n'
    tail = (
        f'        </tbody>\n'
        f'    </table>\n'
        f'</div>\n'
    )
    return head + body + tail


def server_button(label, url):
    i = 12
    text = (
        f'{" " * i}<div class="row">\n'
        f'{" " * i}    <div class="col-4 col-12-small"></div>\n'
        f'{" " * i}    <div class="col-4 col-12-small">\n'
        f'{" " * i}        <a href="{url}" class="button fit">{label}</a>'
        f'{" " * i}    </div>\n'
        f'{" " * i}    <div class="col-4 col-12-small"></div>\n'
        f'{" " * i}</div>\n'
    )
    return text
