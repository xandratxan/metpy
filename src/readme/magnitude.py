"""README file for physical-magnitude package."""
import src.code.physical_magnitude as cd
import src.definitions as df
import src.functions as fnc
from src.readme.template import readme, author_contributor


def code_snippet(import_package, str_m1, str_m2):
    """Template for code snippet section of README file for physical-magnitude package."""
    text = (
        f"```python\n"
        f"{import_package}\n"
        f"\n"
        f"# Define magnitudes\n"
        f"m1 = {str_m1}\n"
        f"m2 = {str_m2}\n"
        f"print(f'm1: {{m1}}')\n"
        f"print(f'm2: {{m2}}')\n"
        f"\n"
        f"# Sum magnitudes\n"
        f"m_sum = m1 + m2\n"
        f"print(f'Sum: {{m_sum}}')\n"
        f"\n"
        f"# Subtract magnitudes\n"
        f"m_dif = m2 - m1\n"
        f"print(f'Subtract: {{m_dif}}')\n"
        f"\n"
        f"# Multiply magnitudes\n"
        f"m_prod = m1 * m2\n"
        f"print(f'Multiply: {{m_prod}}')\n"
        f"m_prod.unit = 'm²'\n"
        f"print(f'Multiply: {{m_prod}}')\n"
        f"\n"
        f"# Divide magnitudes\n"
        f"m_div = m2 / m1\n"
        f"print(f'Divide: {{m_div}}')\n"
        f"m_div.unit = ''\n"
        f"print(f'Divide: {{m_div}}')\n"
        f"```\n"
    )
    return text


def snippet_output(m1, m2, m_sum, m_dif, m_prod1, m_prod2, m_div1, m_div2):
    """Template for code snippet output section of README file for physical-magnitude package."""
    text = (
        f"```\n"
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
        f"Divide: {m_div2}\n"
        f"```\n"
    )
    return text


def release_history():
    """Template for release history section of README file for physical-magnitude package."""
    text = (
        f"* 0.1.0\n"
        f"    * First release\n"
    )
    return text


# README file for physical-magnitude package.
readme = readme(
    name=df.magnitude['name'],
    brief_description=df.magnitude['brief_description'],
    description=df.magnitude['description'],
    last_version=df.magnitude['last_version'],
    last_release=df.magnitude['last_release'],
    license_info=df.magnitude['license'],
    url_source_code=df.magnitude['url_source_code'],
    url_issues=df.magnitude['url_issues'],
    url_documentation=df.magnitude['url_documentation'],
    non_stable_msg=df.non_stable_msg,
    install_from_server=fnc.install_from_server(df.magnitude['name'], df.server['url_server']),
    install_from_github=fnc.install_from_github(df.magnitude['name'], df.xcb['github']),
    install_from_clone=fnc.install_from_clone(df.magnitude['name'], df.xcb['github_username']),
    code_snippet=code_snippet(
        import_package=df.magnitude['import'],
        str_m1=cd.str_m8, str_m2=cd.str_m9),
    snippet_output=snippet_output(
        m1=cd.m8, m2=cd.m9, m_sum=cd.m_sum, m_dif=cd.m_dif,
        m_prod1=cd.m_prod1, m_prod2=cd.m_prod2, m_div1=cd.m_div1, m_div2=cd.m_div2),
    release_history=release_history(),
    authors=author_contributor()
)
