# HTML package pages of MetPy website

import src.definitions as df
import src.functions as fnc
import src.html.templates.base as bs
import src.html.templates.secondary_section as ss
from src.html.main_pages import footer

# HTML physical-magnitude package page
magnitude = bs.base_template(
    title='MetPy-Packages-Physical-magnitude',
    assets=fnc.html_assets(parent=True),
    header=bs.base_header_template(active='projects'),
    main=bs.base_main_template(
        main=ss.package_template(
            title=ss.title_template(
                title=f"{df.magnitude['name']} package",
                brief_description=df.magnitude['brief_description'],
                image_path=fnc.html_images(parent=True),
                image_name=df.magnitude['image']),
            information=ss.info_template(
                last_version=df.magnitude['last_version'],
                last_release=df.magnitude['last_release'],
                license_info=df.magnitude['license'],
                url_source_code=df.magnitude['url_source_code'],
                url_issues=df.magnitude['url_issues'],
                url_documentation=df.magnitude['url_documentation']),
            warning=ss.warning_template(message=df.non_stable_msg),
            description=ss.description_template(description=df.magnitude['description']),
            installation=ss.installation_template(
                is_server=False,
                install_from_server=fnc.install_from_server(
                    package_name=df.magnitude['name'],
                    server_url=df.server['url_server'])),
            code_snippet='Code snippet')),
    footer=footer,
    scripts=bs.base_scripts_template(assets=fnc.html_assets(parent=True)))
