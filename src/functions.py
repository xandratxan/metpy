# Functions to build and update documentation

def html_resources(parent=False, grandparent=False):
    if grandparent:
        path = '../..'
    elif parent:
        path = '..'
    else:
        path = '.'
    return path


def write_files(texts, files):
    # Write documentation source files
    for text, file in zip(texts, files):
        f = open(file, "w")
        f.write(text)
        f.close()


def install_from_server(package_name, server_url):
    # Command for package installation from server
    return f'pip install {package_name} --extra-index-url {server_url}'


def install_from_github(package_name, author_github_url):
    # Command for package installation from GitHub repository
    return f'pip install git+{author_github_url}{package_name}.git#egg={package_name}'


def install_from_clone(package_name, author_github_username):
    # Command for package installation from repository clone
    command = (f" git clone git@github.com:{author_github_username}/{package_name}.git\n"
               f" cd {package_name}\n"
               f" pip install .")
    return command
