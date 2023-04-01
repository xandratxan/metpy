# Base HTML template for MetPy website
import src.definitions as df


def base_template(title, parent, header, main, footer, scripts):
    if parent:
        path = '..'
    else:
        path = '.'
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
        f'    <div id="wrapper">\n'
        f'        {header}'
        f'        {main}'
        f'        {footer}'
        f'    </div>\n'
        f'{scripts}\n'
        f'</body>\n'
        f'</html>\n'
    )
    return text


def base_header_template(parent, active):
    if parent:
        path = '..'
    else:
        path = '.'
    html_index = df.html_pages['main']['index']
    html_packages = df.html_pages['main']['packages']
    html_server = df.html_pages['main']['server']
    html_docs = df.html_pages['main']['docs']
    url_author_github = df.xcb['github']
    active_tab = '<li class="active">'
    inactive_tab = '<li>'
    text = (
        f'        <!-- Header-->\n'
        f'        <header id="header"><a href="{path}/index.html" class="logo">MetPy</a></header>\n'
        f'        <!-- Nav -->'
        f'        <nav id="nav">\n'
        f'            <ul class="links">\n'
        f'                {active_tab if active == "index" else inactive_tab}<a href="{path}/{html_index}">MetPy</a></li>\n'
        f'                {active_tab if active == "packages" else inactive_tab}<a href="{path}/{html_packages}">Packages</a></li>\n'
        f'                {active_tab if active == "server" else inactive_tab}<a href="{path}/{html_server}">Package Server</a></li>\n'
        f'                {active_tab if active == "docs" else inactive_tab}<a href="{path}/{html_docs}">Documentation</a></li>\n'
        f'            </ul>'
        f'            <ul class="icons">\n'
        f'                <li><a href="{url_author_github}" class="icon brands fa-github"><span class="label">GitHub</span></a>\n'
        f'                </li>\n'
        f'            </ul>\n'
        f'        </nav>\n'
    )
    return text


def base_main_template(main):
    text = (
        f'        <!-- Main -->\n'
        f'        <div id="main">\n'
        f'            {main}\n'
        f'        </div>\n'
    )
    return text


def base_footer_template(url_author_github, url_author_email, url_lmri, url_ciemat):
    text = (
        f'        <!-- Footer -->\n'
        f'        <footer id="footer">\n'
        f'            <section class="split contact">\n'
        f'                <section>\n'
        f'                    <h3>ABOUT ME</h3>\n'
        f'                    <p>Xandra Campo<br/>\n'
        f'                       Researcher at the Neutron Standards Laboratory (LPN)<br/>\n'
        f'                       Ionizing Radiation Metrology Laboratory (<a href="{url_lmri}">LMRI</a>)<br/>\n'
        f'                       Research Centre for Energy, Environment and Technology (<a href="{url_ciemat}">CIEMAT</a>)<br/>\n'
        f'                       {url_author_email}</p>\n'
        f'                </section>\n'
        f'                <section>\n'
        f'                    <h3>SOCIAL</h3>\n'
        f'                    <ul class="icons alt">\n'
        f'                        <li><a href="{url_author_github}" class="icon brands alt fa-github"><span class="label">GitHub</span></a></li>\n'
        f'                    </ul>\n'
        f'                </section>\n'
        f'            </section>\n'
        f'        </footer>\n'
        f'        <!-- Copyright -->\n'
        f'        <div id="copyright">\n'
        f'            <ul>\n'
        f'                <li>@ 2023, Xandra Campo</li>\n'
        f'                <li>Design: <a href="https://html5up.net">HTML5 UP</a></li>\n'
        f'                <li><a href="https://www.flaticon.com/" title="python icons">Icons: Freepik</a></li>\n'
        f'            </ul>\n'
        f'        </div>\n'
    )
    return text


def base_scripts_template(parent):
    if parent:
        path = '..'
    else:
        path = '.'
    text = (
        f'    <!-- Scripts -->\n'
        f'    <script src="{path}/assets/js/jquery.min.js"></script>\n'
        f'    <script src="{path}/assets/js/jquery.scrollex.min.js"></script>\n'
        f'    <script src="{path}/assets/js/jquery.scrolly.min.js"></script>\n'
        f'    <script src="{path}/assets/js/browser.min.js"></script>\n'
        f'    <script src="{path}/assets/js/breakpoints.min.js"></script>\n'
        f'    <script src="{path}/assets/js/util.js"></script>\n'
        f'    <script src="{path}/assets/js/main.js"></script>\n'
        f'    <script src="{path}/assets/js/prism.js"></script>\n'
    )
    return text
