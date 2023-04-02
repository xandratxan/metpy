"""Base HTML templates for MetPy website."""
import src.definitions as df
import src.functions as fnc


def base_template(title, header, main, footer, scripts, parent=False, grandparent=False):
    """Base HTML template for MetPy website."""
    path = fnc.html_resources(parent=parent, grandparent=grandparent)
    text = (
        f'<!DOCTYPE HTML>\n'
        f'<html lang="en">\n'
        f'<head>\n'
        f'    <title>{title}</title>\n'
        f'    <meta charset="utf-8"/>\n'
        f'    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no"/>\n'
        f'    <link rel="stylesheet" href="{path}/assets/css/main.css"/>\n'
        f'    <link rel="stylesheet" href="{path}/assets/css/prism.css"/>\n'
        f'    <noscript>\n'
        f'        <link rel="stylesheet" href="{path}/assets/css/noscript.css"/>\n'
        f'    </noscript>\n'
        f'</head>\n'
        f'<body class="is-preload">\n'
        f'    <!-- Wrapper -->\n'
        f'    <div id="wrapper" class="fade-in">\n'
        f'{header}'
        f'{main}'
        f'{footer}'
        f'    </div>\n'
        f'{scripts}'
        f'</body>\n'
        f'</html>\n'
    )
    return text


def base_header_template(active, parent=False, grandparent=False):
    """Template for header section of base HTML templates for MetPy website."""
    i = 8
    path = fnc.html_resources(parent=parent, grandparent=grandparent)
    html_index = df.html_pages['index']
    html_packages = df.html_pages['packages']['index']
    html_server = df.html_pages['server']['index']
    html_docs = df.html_pages['documentation']['index']
    url_author_github = df.xcb['github']
    text = (
        f'{" " * i}<!-- Header-->\n'
        f'{" " * i}<header id="header"><a href="{path}/index.html" class="logo">MetPy</a></header>\n'
        f'{" " * i}<!-- Nav -->\n'
        f'{" " * i}<nav id="nav">\n'
        f'{" " * i}    <ul class="links">\n'
        f'{" " * i}        {active_tab(active, "index")}<a href="{path}/{html_index}">MetPy</a></li>\n'
        f'{" " * i}        {active_tab(active, "packages")}<a href="{path}/{html_packages}">Packages</a></li>\n'
        f'{" " * i}        {active_tab(active, "server")}<a href="{path}/{html_server}">Package Server</a></li>\n'
        f'{" " * i}        {active_tab(active, "docs")}<a href="{path}/{html_docs}">Documentation</a></li>\n'
        f'{" " * i}    </ul>\n'
        f'{" " * i}    <ul class="icons">\n'
        f'{" " * i}        <li>\n'
        f'{" " * i}            <a href="{url_author_github}" class="icon brands fa-github">\n'
        f'{" " * i}            <span class="label">GitHub</span></a>\n'
        f'{" " * i}        </li>\n'
        f'{" " * i}    </ul>\n'
        f'{" " * i}</nav>\n'
    )
    return text


def active_tab(active, tab):
    return '<li class="active">' if active == tab else '<li>'


def base_main_template(main):
    """Template for main section of base HTML templates for MetPy website."""
    i = 8
    text = (
        f'{" " * i}<!-- Main -->\n'
        f'{" " * i}<div id="main">\n'
        f'{main}'
        f'{" " * i}</div>\n'
    )
    return text


def base_footer_template():
    """Template for footer section of base HTML templates for MetPy website."""
    url_author_github = df.xcb['github']
    url_author_email = df.xcb['email']
    url_lmri = df.external_urls['lmri']
    url_ciemat = df.external_urls['ciemat']
    url_design = df.external_urls['design']
    url_icons = df.external_urls['icons']
    i = 8
    text = (
        f'{" " * i}<!-- Footer -->\n'
        f'{" " * i}<footer id="footer">\n'
        f'{" " * i}    <section class="split contact">\n'
        f'{" " * i}        <section>\n'
        f'{" " * i}            <h3>About me</h3>\n'
        f'{" " * i}            <p>Xandra Campo<br/>\n'
        f'{" " * i}               Researcher at the Neutron Standards Laboratory (LPN)</p>\n'
        f'{" " * i}        </section>\n'
        f'{" " * i}        <section>\n'
        f'{" " * i}            <h3>Affiliation</h3>\n'
        f'{" " * i}            <p>Neutron Standards Laboratory (LPN)<br/>\n'
        f'{" " * i}               Ionizing Radiation Metrology Laboratory\n'
        f'{" " * i}               (<a href="{url_lmri}">LMRI</a>)<br/>\n'
        f'{" " * i}               Research Centre for Energy, Environment and Technology\n'
        f'{" " * i}               (<a href="{url_ciemat}">CIEMAT</a>)</p>\n'
        f'{" " * i}        </section>\n'
        f'{" " * i}        <section>\n'
        f'{" " * i}            <h3>Contact</h3>\n'
        f'{" " * i}            <p>{url_author_email}</p>\n'
        f'{" " * i}        </section>\n'
        f'{" " * i}        <section>\n'
        f'{" " * i}            <h3>Social</h3>\n'
        f'{" " * i}            <ul class="icons alt">\n'
        f'{" " * i}                <li>\n'
        f'{" " * i}                    <a href="{url_author_github}" class="icon brands alt fa-github">\n'
        f'{" " * i}                    <span class="label">GitHub</span></a>\n'
        f'{" " * i}                </li>\n'
        f'{" " * i}            </ul>\n'
        f'{" " * i}        </section>\n'
        f'{" " * i}    </section>\n'
        f'{" " * i}</footer>\n'
        f'{" " * i}<!-- Copyright -->\n'
        f'{" " * i}<div id="copyright">\n'
        f'{" " * i}    <ul>\n'
        f'{" " * i}        <li>@ 2023, Xandra Campo</li>\n'
        f'{" " * i}        <li>Design: <a href="{url_design}">HTML5 UP</a></li>\n'
        f'{" " * i}        <li><a href="{url_icons}" title="python icons">Icons: Freepik</a></li>\n'
        f'{" " * i}    </ul>\n'
        f'{" " * i}</div>\n'
    )
    return text


def base_scripts_template(parent=False, grandparent=False):
    """Template for scripts section of base HTML templates for MetPy website."""
    i = 4
    path = fnc.html_resources(parent=parent, grandparent=grandparent)
    text = (
        f'{" " * i}<!-- Scripts -->\n'
        f'{" " * i}<script src="{path}/assets/js/jquery.min.js"></script>\n'
        f'{" " * i}<script src="{path}/assets/js/jquery.scrollex.min.js"></script>\n'
        f'{" " * i}<script src="{path}/assets/js/jquery.scrolly.min.js"></script>\n'
        f'{" " * i}<script src="{path}/assets/js/browser.min.js"></script>\n'
        f'{" " * i}<script src="{path}/assets/js/breakpoints.min.js"></script>\n'
        f'{" " * i}<script src="{path}/assets/js/util.js"></script>\n'
        f'{" " * i}<script src="{path}/assets/js/main.js"></script>\n'
        f'{" " * i}<script src="{path}/assets/js/prism.js"></script>\n'
    )
    return text
