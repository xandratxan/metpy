"""HTML server pages of MetPy website."""
import src.definitions as df
import src.functions as fnc
import src.html.templates.base as bs
import src.html.templates.secondary_section as ss

# Packages
magnitude = {
    'name': df.magnitude['name'],
    'brief_description': df.magnitude['brief_description'],
    'html_path': df.html_pages['server']['magnitude'],
    'image': df.magnitude['image'],
    'versions': fnc.versions(df.magnitude['named_versions']),
}
# MetPy website server page
server = bs.base_template(
    parent=True,
    title='MetPy-Package Server',
    header=bs.base_header_template(active='server', parent=True),
    main=bs.base_main_template(
        main=ss.server_template(
            title=ss.title_template(
                parent=True,
                title='Python package server',
                brief_description=df.server['brief_description'],
                image=df.server['image']
            ),
            warning='',
            description=ss.server_description_template(),
            installation=ss.installation_template(
                is_server=True,
                install_from_server=fnc.install_from_server(
                    package_name='package_name',
                    server_url=df.server['url_server']
                )
            ),
            packages_table=ss.packages_table_template(
                parent=True,
                columns=['Package', 'Description'],
                packages=[magnitude]
            ),
        )
    ),
    footer=bs.base_footer_template(),
    scripts=bs.base_scripts_template(parent=True)
)
# MetPy server packages, physical-magnitude package page
server_magnitude = bs.base_template(
    grandparent=True,
    title='MetPy-Package Server',
    header=bs.base_header_template(active='server', grandparent=True),
    main=bs.base_main_template(
        main=ss.server_template(
            title=ss.title_template(
                grandparent=True,
                title=f"Physical magnitude package",
                brief_description=df.magnitude['brief_description'],
                image=df.magnitude['image'],
            ),
            warning=ss.warning_template(message=df.non_stable_msg),
            description=ss.description_template(
                name=df.magnitude['name'],
                description=df.magnitude['description']),
            installation=ss.installation_template(
                is_server=False,
                install_from_server=fnc.install_from_server(
                    package_name=df.magnitude['name'],
                    server_url=df.server['url_server']
                )
            ),
            packages_table=ss.packages_table_template(
                grandparent=True,
                versions=True,
                columns=['Package', 'Version'],
                packages=magnitude
            ),
        )
    ),
    footer=bs.base_footer_template(),
    scripts=bs.base_scripts_template(grandparent=True))
