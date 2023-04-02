"""RST templates for package documentation API."""


def api_template(name, api):
    text = (
        f"API Reference\n"
        f"=============\n"
        f"\n"
        f"This part of the documentation covers all the public interfaces of ``{name}``.\n"
        f"\n"
        f"{api}"
    )
    return text
