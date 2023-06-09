"""RST files for physical-magnitude documentation."""
import src.definitions as df
import src.rst.templates.templates as tmp
import src.rst.templates.magnitude as mag
import src.functions as fnc
import src.code.physical_magnitude as cd

# RST index file for physical-magnitude package
index = tmp.index_template(
    name=df.magnitude['name'],
    description=df.magnitude['description'],
    non_stable_msg=df.non_stable_msg,
    versions=df.magnitude['named_versions'],
    contributors=True,
    last_version=fnc.last_version(df.magnitude['named_versions']),
    license_info=df.magnitude['license'],
    url_source_code=df.magnitude['url_source_code'],
    url_issues=df.magnitude['url_issues'],
)
# RST API file for physical-magnitude package
api = tmp.api_template(
    name=df.magnitude['name'],
    api=mag.api()
)
# RST tutorial file for physical-magnitude package
tutorial = tmp.tutorial_template(
    name=df.magnitude['name'],
    install_from_server=fnc.install_from_server(df.magnitude['name'], df.server['url_server']),
    install_from_github=fnc.install_from_github(df.magnitude['name'], df.xcb['github']),
    install_from_clone=fnc.install_from_clone(df.magnitude['name'], df.xcb['github_username']),
    tutorial=mag.tutorial(df.magnitude['import'], *cd.tutorial)
)
# RST how-to file for physical-magnitude package
howto = tmp.howto_template(
    name=df.magnitude['name'],
    howto=mag.howto(*cd.howto)
)
