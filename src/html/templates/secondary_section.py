# HTML templates for secondary sections at MetPy website

def package_template(title, information, warning, description, installation, code_snippet):
    # Template for package page at MetPy website
    text = (
        f'<!-- Package -->\n'
        f'<section class="post">\n'
        f'    {title}\n'
        f'    {information}\n'
        f'    {warning}\n'
        f'    {description}\n'
        f'    {installation}\n'
        f'    {code_snippet}\n'
        f'</section>\n'
    )
    return text


def title_template(title, brief_description, image_path, image_name):
    # Template for section pages at my website at GitHub Pages (package server page and package pages)
    text = (
        f'<!-- Title and subtitle -->\n'
        f'<header class="major">\n'
        f'    <h1>{title}</h1>\n'
        f'    <p>{brief_description}</p>\n'
        f'    <img src="{image_path}{image_name}" alt="" width="100" height="100">\n'
        f'</header>\n'
    )
    return text


def info_template(last_version, last_release, license_info, url_source_code, url_issues, url_documentation):
    # Template for section pages at my website at GitHub Pages (package server page and package pages)
    text = (
        f'<!-- Useful information -->\n'
        f'<div class="box">\n'
        f'    <div class="row">\n'
        f'        <div class="col-4 col-12-small">\n'
        f'            <b>Last version</b>: {last_version}<br/>\n'
        f'            <b>Last release</b>: {last_release}\n'
        f'        </div>\n'
        f'        <div class="col-4 col-12-small">\n'
        f'            <b>Source code</b>: <a href="{url_source_code}">GitHub</a><br/>\n'
        f'            <b>Documentation</b>: <a href="{url_documentation}">GitHub</a>\n'
        f'        </div>\n'
        f'        <div class="col-3 col-12-small">\n'
        f'            <b>Issues</b>: <a href="{url_issues}">GitHub</a><br/>\n'
        f'            <b>License</b>: {license_info}\n'
        f'        </div>\n'
        f'    </div>\n'
        f'</div>\n'
    )
    return text


def warning_template(message):
    # Template for section pages at my website at GitHub Pages (package server page and package pages)
    text = (
        f'<!-- Warning -->\n'
        f'<div class="box">\n'
        f'    <p><b>WARNING</b>: {message}</p>\n'
        f'</div>\n'
    )
    return text


def description_template(description):
    text = (
        f'    <!-- Description -->\n'
        f'    <p>{description}</p>\n'
    )
    return text


def installation_template(is_server, install_from_server):
    # Template for section of package pages at my website at GitHub Pages
    if is_server:
        text = (
            f'<!-- Installation -->\n'
            f'<p>The packages available in this server can be used to specify dependencies in\n'
            f'   <code>pyproject.toml</code> files including the entry <code>dependencies = ["package-name"]</code>\n'
            f'   They can also be installed via <code>pip</code>:<br/>\n'
            f'   <code>{install_from_server}</code></p>\n'
        )
    else:
        text = (
            f'<!-- Installation -->\n'
            f'<p>This package can be installed via <code>pip</code>:<br/>\n'
            f'   <code>{install_from_server}</code></p>\n'
        )
    return text


def code_snippet_template(name, code, output):
    # Template for section of package pages at my website at GitHub Pages
    text = (
        f'<!-- Code snippet -->\n'
        f'<p>Below you can find a code snippet to illustrate how to work with <code>{name}</code> package:</p>\n'
        f'<pre><code class="language-python line-numbers" data-prismjs-copy="Copy">{code}</code></pre>\n'
        f'<p>Below you can find the snippet output:</p>\n'
        f'<pre><code class="language-python line-numbers" data-prismjs-copy="Copy">{output}</code></pre>\n'
    )
    return text


def packages_table_template(package_server_link, columns, packages):
    # Template for packages table in the section of package server page at my website at GitHub Pages
    head = (
        f'<!-- Packages -->\n'
        f'<p>The following packages are available:</p>\n'
        f'<div class="table-wrapper">\n'
        f'    <table>\n'
        f'        <thead>\n'
        f'            <tr>\n'
        f'                <th></th>\n'
        f'                <th>{columns[0]}</th>\n'
        f'                <th>{columns[1]}</th>\n'
        f'            </tr>\n'
        f'        </thead>\n'
        f'        <tbody>\n'
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
    text = (
        f'<div class="row">\n'
        f'    <div class="col-4 col-12-small"></div>\n'
        f'    <div class="col-4 col-12-small">\n'
        f'        <a href="{url}" class="button fit">{label}</a>'
        f'    </div>\n'
        f'    <div class="col-4 col-12-small"></div>\n'
        f'</div>\n'
    )
    return text
