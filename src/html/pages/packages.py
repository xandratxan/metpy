"""HTML package pages of MetPy website."""
import src.code.physical_magnitude as cd
import src.definitions as df
import src.functions as fnc
import src.html.templates.base as bs
import src.html.templates.main_section as ms
import src.html.templates.secondary_section as ss
from src.html.pages.index import footer

# MetPy website packages page
# TODO: cards not showing side by side
magnitude = {
    'name': 'magnitude',
    'title': f"{df.magnitude['name']} package",
    'brief_description': df.magnitude['brief_description'],
    'html_path': df.html_pages['packages']['magnitude'],
    'image': df.magnitude['image']
}
metpy_packages = bs.base_template(
    title='MetPy-Packages',
    header=bs.base_header_template(active='packages'),
    main=bs.base_main_template(
        main=ms.main_section_template(
            title='MetPy Packages',
            description=(f'MetPy includes a set of Python packages useful for metrology applications. '
                         f'Here you can find the packages of the MetPy ecosystem.'),
            image='python.png',
            cards=[magnitude]
        )
    ),
    footer=footer,
    scripts=bs.base_scripts_template()
)


# MetPy website packages, physical-magnitude package page
def html_code_snippet(import_package, str_m1, str_m2):
    text = (
        f'{import_package}\n'
        f'\n'
        f'# Define magnitudes\n'
        f'm1 = {str_m1}\n'
        f'm2 = {str_m2}\n'
        f'print(f"m1: {{m1}}")\n'
        f'print(f"m2: {{m2}}")\n'
        f'\n'
        f'# Sum magnitudes\n'
        f'm_sum = m1 + m2\n'
        f'print(f"Sum: {{m_sum}}")\n'
        f'\n'
        f'# Subtract magnitudes\n'
        f'm_dif = m2 - m1\n'
        f'print(f"Subtract: {{m_dif}}")\n'
        f'\n'
        f'# Multiply magnitudes\n'
        f'm_prod = m1 * m2\n'
        f'print(f"Multiply: {{m_prod}}")\n'
        f'm_prod.unit = "m²"\n'
        f'print(f"Multiply: {{m_prod}}")\n'
        f'\n'
        f'# Divide magnitudes\n'
        f'm_div = m2 / m1\n'
        f'print(f"Divide: {{m_div}}")\n'
        f'm_div.unit = ''\n'
        f'print(f"Divide: {{m_div}}")'
    )
    return text


def html_snippet_output(m1, m2, m_sum, m_dif, m_prod1, m_prod2, m_div1, m_div2):
    text = (
        f"m1: {m1}\n"
        f"m2: {m2}\n"
        f"\n"
        f"Sum: {m_sum}\n"
        f"\n"
        f"Subtract: {m_dif})\n"
        f"\n"
        f"Multiply: {m_prod1}\n"
        f"Multiply: {m_prod2}\n"
        f"\n"
        f"Divide: {m_div1}\n"
        f"Divide: {m_div2}"
    )
    return text


metpy_package_magnitude = bs.base_template(
    parent=True,
    title='MetPy-Packages-Physical-magnitude',
    header=bs.base_header_template(active='packages', parent=True),
    main=bs.base_main_template(
        main=ss.package_template(
            title=ss.title_template(
                parent=True,
                title=f"{df.magnitude['name']} package",
                brief_description=df.magnitude['brief_description'],
                image=df.magnitude['image']
            ),
            information=ss.info_template(
                last_version=df.magnitude['last_version'],
                last_release=df.magnitude['last_release'],
                license_info=df.magnitude['license'],
                url_source_code=df.magnitude['url_source_code'],
                url_issues=df.magnitude['url_issues'],
                url_documentation=df.magnitude['url_documentation']
            ),
            warning=ss.warning_template(message=df.non_stable_msg),
            description=ss.description_template(description=df.magnitude['description']),
            installation=ss.installation_template(
                is_server=False,
                install_from_server=fnc.install_from_server(
                    package_name=df.magnitude['name'],
                    server_url=df.server['url_server']
                )
            ),
            code_snippet=ss.code_snippet_template(
                name=df.magnitude['name'],
                code=html_code_snippet(
                    import_package=df.magnitude['import'],
                    str_m1=cd.str_m8, str_m2=cd.str_m9
                ),
                output=html_snippet_output(
                    m1=cd.m8, m2=cd.m9, m_sum=cd.m_sum, m_dif=cd.m_dif,
                    m_prod1=cd.m_prod1, m_prod2=cd.m_prod2, m_div1=cd.m_div1, m_div2=cd.m_div2
                )
            ),
        )
    ),
    footer=footer,
    scripts=bs.base_scripts_template(parent=True)
)
