"""index.rst for physical-magnitude documentation."""
import src.definitions as df
from src.rst.templates.index import index

package_magnitude_index = index(
    name=df.magnitude['name'],
    description=df.magnitude['description'],
    non_stable_msg=df.non_stable_msg,
    versions=df.magnitude['named_versions'],
    contributors=True,
    last_version=df.magnitude['last_version'],
    last_release=df.magnitude['last_release'],
    license_info=df.magnitude['license'],
    url_source_code=df.magnitude['url_source_code'],
    url_issues=df.magnitude['url_issues'],
    url_documentation=df.magnitude['url_documentation']
)
